"""
Refactor Agent - Creates React components with Tailwind CSS styling
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any

class RefactorAgent:
    """Agent responsible for creating React components"""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    def create_component(self, component_info: Dict[str, Any], user_brief: str) -> str:
        print("🛠️ Creating component...", component_info["name"])
        """Create a React component with Tailwind CSS"""
        
        name = component_info["name"]
        description = component_info["description"]
        design_config = component_info["design_config"]
        
        # Create design context from config
        color_scheme = design_config.get("color_scheme", {})
        typography = design_config.get("typography", {})
        spacing = design_config.get("spacing", {})
        
        prompt = f"""
        You are a React Component Refactor Agent. Create a React functional component using Tailwind CSS.
        
        Component Name: {name}
        Component Description: {description}
        User Brief: {user_brief}
        
        Design Configuration:
        - Primary Color: {color_scheme.get('primary', 'blue-600')}
        - Secondary Color: {color_scheme.get('secondary', 'gray-100')}
        - Accent Color: {color_scheme.get('accent', 'green-500')}
        - Text Color: {color_scheme.get('text', 'gray-900')}
        - Heading Style: {typography.get('heading', 'text-4xl font-bold')}
        - Body Style: {typography.get('body', 'text-base')}
        - Section Spacing: {spacing.get('section', 'py-16')}
        - Container Style: {spacing.get('container', 'px-4 mx-auto max-w-6xl')}
        
        Create a complete React component that:
        1. Uses modern Tailwind CSS classes
        2. Is responsive and mobile-friendly
        3. Matches the design configuration
        4. Includes realistic placeholder content
        5. Follows React best practices
        
        Return ONLY the React component code, no explanations.
        Start with: import React from 'react';
        """
        
        try:
            response = self.llm.invoke(prompt)
            component_code = response.content.strip()
            
            # Clean up the response to ensure it's valid React code
            if not component_code.startswith('import'):
                # Add import if missing
                component_code = f"import React from 'react';\n\n{component_code}"
            
            return component_code
            
        except Exception as e:
            print(f"❌ Error in RefactorAgent for {name}: {str(e)}")
            return self.get_fallback_component(name, description, design_config)
    
    def get_fallback_component(self, name: str, description: str, design_config: Dict[str, Any]) -> str:
        """Generate a simple fallback component"""
        
        color_scheme = design_config.get("color_scheme", {})
        typography = design_config.get("typography", {})
        spacing = design_config.get("spacing", {})
        
        primary_color = color_scheme.get('primary', 'blue-600')
        heading_style = typography.get('heading', 'text-4xl font-bold')
        body_style = typography.get('body', 'text-base')
        section_spacing = spacing.get('section', 'py-16')
        container_style = spacing.get('container', 'px-4 mx-auto max-w-6xl')
        
        return f"""import React from 'react';

const {name} = () => {{
  return (
    <section className="bg-white {section_spacing}">
      <div className="{container_style}">
        <div className="text-center">
          <h2 className="{heading_style} text-{primary_color} mb-4">
            {name}
          </h2>
          <p className="{body_style} text-gray-600 mb-8">
            {description}
          </p>
          <div className="bg-{primary_color} text-white px-6 py-3 rounded-lg inline-block">
            Learn More
          </div>
        </div>
      </div>
    </section>
  );
}};

export default {name};
"""