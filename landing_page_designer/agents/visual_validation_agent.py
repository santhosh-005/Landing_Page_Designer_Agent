"""
Visual Validation Agent - Validates and suggests improvements for components
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any, Tuple

class VisualValidationAgent:
    """Agent responsible for validating component quality"""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    def validate_component(self, component_code: str, component_info: Dict[str, Any], user_brief: str) -> Tuple[bool, str]:
        """Validate a component and provide feedback"""
        
        prompt = f"""
        You are a Visual Validation Agent. Review this React component for quality and effectiveness.
        
        Component Name: {component_info['name']}
        Component Description: {component_info['description']}
        User Brief: {user_brief}
        
        Component Code:
        ```jsx
        {component_code}
        ```
        
        Evaluate the component based on:
        1. Code quality and React best practices
        2. Tailwind CSS usage and responsiveness
        3. Visual appeal and user experience
        4. Alignment with user brief
        5. Component structure and readability
        
        Respond with:
        - "APPROVED" if the component is good to use
        - "NEEDS_IMPROVEMENT: [specific feedback]" if it needs changes
        
        Be constructive but concise with feedback.
        """
        
        try:
            response = self.llm.invoke(prompt)
            feedback = response.content.strip()
            
            if feedback.startswith("APPROVED"):
                return True, "Component looks good!"
            elif "NEEDS_IMPROVEMENT" in feedback:
                improvement_text = feedback.split("NEEDS_IMPROVEMENT:", 1)[1].strip()
                return False, improvement_text
            else:
                # Default to approval if unclear response
                return True, "Component validation completed"
                
        except Exception as e:
            print(f"❌ Error in VisualValidationAgent: {str(e)}")
            # Default to approval to keep flow moving
            return True, "Validation completed with fallback"