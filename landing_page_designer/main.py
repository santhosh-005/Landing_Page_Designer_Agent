"""
Landing Page Designer Agent - Main Application
A multi-agent system for designing landing pages using LangGraph
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

load_dotenv()

from agents.graph import create_workflow
from utils.file_manager import ComponentFileManager

def main():
    """Main entry point for the Landing Page Designer Agent"""
    print("🚀 Landing Page Designer Agent MVP v1.0")
    print("=" * 50)
    
    # Get user input
    user_brief = input("\n📝 Please provide your landing page brief: ")
    # inspiration = input("💡 Any inspiration or specific requirements: ")
    inspiration ="white theme with pink accents and minimalist design"
    site_name = input("🏷️ Enter a site name (optional): ").strip() or None
    
    # Initialize file manager with unique folder
    file_manager = ComponentFileManager(site_name)
    
    # Create the workflow
    workflow = create_workflow()
    
    # Prepare initial state
    initial_state = {
        "user_brief": user_brief,
        "inspiration": inspiration,
        "sections": [],
        "design_config": {},
        "components": [],
        "current_component_index": 0,
        "file_manager": file_manager
    }
    
    print("\n🔄 Starting the design process...")
    
    try:
        # Run the workflow
        final_state = workflow.invoke(initial_state)
        
        print("\n✅ Landing page design completed!")
        print(f"📁 Components created in: {file_manager.components_path}")
        print(f"📄 App.jsx updated with new components")
        
    except Exception as e:
        print(f"error from main.py \n❌ Error occurred: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    main()