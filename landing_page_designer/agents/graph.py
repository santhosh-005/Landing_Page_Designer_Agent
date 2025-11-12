"""
LangGraph workflow for Landing Page Designer Agent
"""

from langgraph.graph import StateGraph, END
from typing import Dict, Any, List
import json

from .planner_agent import PlannerAgent
from .design_architect_agent import DesignArchitectAgent
from .component_search_agent import ComponentSearchAgent
from .refactor_agent import RefactorAgent
from .visual_validation_agent import VisualValidationAgent


class WorkflowState:
    """State management for the workflow"""
    
    def __init__(self):
        self.user_brief: str = ""
        self.inspiration: str = ""
        self.sections: List[Dict[str, Any]] = []
        self.design_config: Dict[str, Any] = {}
        self.components: List[Dict[str, Any]] = []
        self.current_component_index: int = 0
        self.file_manager = None
        self.max_iterations: int = 3


def planner_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Planner Agent Node"""
    print("🎯 Running Planner Agent...")
    
    planner = PlannerAgent()
    planning_result = planner.plan_sections(state["user_brief"], state["inspiration"])
    
    # Handle both "sections" and "components" keys for backward compatibility
    if "components" in planning_result:
        state["sections"] = planning_result["components"]
    else:
        state["sections"] = planning_result.get("sections", [])
    
    print(f"📋 Planned {len(state['sections'])} sections")
    
    return state


def design_architect_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Design Architect Agent Node"""
    print("🎨 Running Design Architect Agent...")
    
    architect = DesignArchitectAgent()
    design_config = architect.create_design_config(
        state["user_brief"], 
        state["inspiration"], 
        state["sections"]
    )
    
    state["design_config"] = design_config
    print("🎨 Design configuration created")
    
    return state


def component_search_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Component Search Agent Node"""
    print("🔍 Running Component Search Agent...")
    
    search_agent = ComponentSearchAgent()
    components = []
    
    for section in state["sections"]:
        component_info = search_agent.search_components(section, state["design_config"])
        components.append(component_info)
    
    state["components"] = components
    state["current_component_index"] = 0
    print(f"🔍 Prepared {len(components)} components for processing")
    
    return state


def refactor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Refactor Agent Node - Creates component and immediately writes to file"""
    current_index = state["current_component_index"]
    components = state["components"]
    
    if current_index >= len(components):
        return state
    
    current_component = components[current_index]
    print(f"🔧 Creating component: {current_component['name']}")
    
    refactor_agent = RefactorAgent()
    component_code = refactor_agent.create_component(current_component, state["user_brief"])
    
    # Immediately write component to file
    file_manager = state["file_manager"]
    success = file_manager.create_component(current_component["name"], component_code)
    
    if success:
        # Track created components for App.jsx update
        if "created_components" not in state:
            state["created_components"] = []
        state["created_components"].append(current_component["name"])
        
        # Update App.jsx immediately with all created components so far
        file_manager.update_app_jsx(state["created_components"])
        print(f"📄 Component {current_component['name']} created and App.jsx updated")
        # Advance to next component so we don't recreate the same one
        state["current_component_index"] = state.get("current_component_index", 0) + 1
    
    # Mark as processed (no need to store code in memory)
    current_component["processed"] = True
    
    return state


# VALIDATION NODE COMMENTED OUT FOR SIMPLIFIED WORKFLOW
# def validation_node(state: Dict[str, Any]) -> Dict[str, Any]:
#     """Visual Validation Agent Node"""
#     current_index = state["current_component_index"]
#     components = state["components"]
#     
#     if current_index >= len(components):
#         return state
#         
#     current_component = components[current_index]
#     print(f"✅ Validating component: {current_component['name']}")
#     
#     validation_agent = VisualValidationAgent()
#     is_approved, feedback = validation_agent.validate_component(
#         current_component["code"],
#         current_component,
#         state["user_brief"]
#     )
#     
#     current_component["is_approved"] = is_approved
#     current_component["feedback"] = feedback
#     
#     print(f"📝 Validation result: {'Approved' if is_approved else 'Needs improvement'}")
#     if not is_approved:
#         print(f"💡 Feedback: {feedback}")
#     
#     return state


def should_iterate_component(state: Dict[str, Any]) -> str:
    """Simplified: Just move to next component or finalize"""
    current_index = state["current_component_index"]
    components = state["components"]
    # Decide the next step based on current index (refactor_node already advances index)
    if current_index >= len(components):
        return "finalize"
    else:
        return "refactor"  # Create next component


def finalize_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Finalize the workflow - components are already created"""
    print("🎉 Finalizing workflow...")
    
    created_components = state.get("created_components", [])
    print(f"✅ Successfully processed {len(created_components)} components")
    
    if created_components:
        print(f"📄 Created components: {', '.join(created_components)}")
        print("📱 App.jsx has been updated with all components")
    
    return state


def create_workflow() -> StateGraph:
    """Create the LangGraph workflow"""
    
    # Create the graph
    workflow = StateGraph(dict)
    
    # Add nodes - removed validation for simplified workflow
    workflow.add_node("planner", planner_node)
    workflow.add_node("design_architect", design_architect_node)
    workflow.add_node("component_search", component_search_node)
    workflow.add_node("refactor", refactor_node)
    workflow.add_node("finalize", finalize_node)
    
    # Define edges - Simplified workflow without validation loop
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "design_architect")
    workflow.add_edge("design_architect", "component_search")
    workflow.add_edge("component_search", "refactor")
    
    # Conditional edge to create all components
    workflow.add_conditional_edges(
        "refactor",
        should_iterate_component,
        {
            "refactor": "refactor",
            "finalize": "finalize"
        }
    )
    
    workflow.add_edge("finalize", END)
    
    # Compile the workflow
    return workflow.compile()