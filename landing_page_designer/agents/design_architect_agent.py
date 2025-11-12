"""
Design Architect Agent - Creates design configuration for the entire landing page
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any

class DesignArchitectAgent:
    """Agent responsible for creating overall design configuration"""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    def create_design_config(self, user_brief: str, inspiration: str, sections: list) -> Dict[str, Any]:
        """Create design configuration for the landing page"""
        
        sections_list = "\n".join([f"- {section['name']}: {section['description']}" for section in sections])
        
        prompt = f"""
        You are a Design Architect Agent. Create a comprehensive design configuration for a landing page.
        
        User Brief: {user_brief}
        Inspiration: {inspiration}
        
        Planned Sections:
        {sections_list}
        
        Please provide a JSON response with design configuration:
        {{
            "color_scheme": {{
                "primary": "blue-600",
                "secondary": "gray-100",
                "accent": "green-500",
                "text": "gray-900"
            }},
            "typography": {{
                "heading": "text-4xl font-bold",
                "subheading": "text-xl font-semibold",
                "body": "text-base",
                "small": "text-sm"
            }},
            "spacing": {{
                "section": "py-16",
                "container": "px-4 mx-auto max-w-6xl",
                "element": "mb-8"
            }},
            "layout": {{
                "hero_layout": "center",
                "features_layout": "grid",
                "grid_cols": "grid-cols-3"
            }}
        }}
        
        Use Tailwind CSS classes and keep it modern and clean.
        """
        
        try:
            response = self.llm.invoke(prompt)
            content = response.content
            
            # Extract JSON from response
            import json
            import re
            
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                design_config = json.loads(json_match.group())
                return design_config
            else:
                # Fallback design config
                return self.get_default_design_config()
                
        except Exception as e:
            print(f"❌ Error in DesignArchitectAgent: {str(e)}")
            return self.get_default_design_config()
    
    def get_default_design_config(self) -> Dict[str, Any]:
        """Return default design configuration"""
        return {
            "color_scheme": {
                "primary": "blue-600",
                "secondary": "gray-100",
                "accent": "green-500",
                "text": "gray-900"
            },
            "typography": {
                "heading": "text-4xl font-bold",
                "subheading": "text-xl font-semibold",
                "body": "text-base",
                "small": "text-sm"
            },
            "spacing": {
                "section": "py-16",
                "container": "px-4 mx-auto max-w-6xl",
                "element": "mb-8"
            },
            "layout": {
                "hero_layout": "center",
                "features_layout": "grid",
                "grid_cols": "grid-cols-3"
            }
        }