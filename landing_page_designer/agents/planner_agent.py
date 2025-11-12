"""
Planner Agent - Decides what sections are needed and in what order
"""
import json
import re
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any

class PlannerAgent:
    """Agent responsible for planning the landing page sections"""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    def plan_sections(self, user_brief: str, inspiration: str) -> Dict[str, Any]:
        """Plan the sections needed for the landing page"""
        
        prompt = f"""
        You are a Landing Page Planner Agent. Based on the user's brief and inspiration, 
        plan the sections needed for an effective landing page.
        
        User Brief: {user_brief}
        Inspiration: {inspiration}
        
        Please provide a JSON response with the following structure:
        {{
            "sections": [
                {{
                    "name": "Header",
                    "order": 1,
                    "description": "Navigation and hero section with main headline"
                }},
                {{
                    "name": "Features",
                    "order": 2,
                    "description": "Key features or benefits"
                }}
            ]
        }}
        
        Keep it simple and effective. Common sections include: Header, Hero, Features, About, Testimonials, CTA, Footer.
        Focus on 3-5 main sections for an MVP.
        """
        
        try:
            response = self.llm.invoke(prompt)
            content = response.content
            
            # Extract JSON from response
            print("📝 Planning sections...", content)
            # exit()
            
            # Try to find JSON in the response
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                sections_data = json.loads(json_match.group())
                return sections_data
            else:
                # Fallback plan if JSON parsing fails
                return {
                    "sections": [
                        {"name": "Header", "order": 1, "description": "Navigation and main headline"},
                        {"name": "Hero", "order": 2, "description": "Main value proposition"},
                        {"name": "Features", "order": 3, "description": "Key features or benefits"},
                        {"name": "CallToAction", "order": 4, "description": "Call to action section"}
                    ]
                }
                
        except Exception as e:
            print(f"❌ Error in PlannerAgent: {str(e)}")
            # Return default plan
            return {
                "sections": [
                    {"name": "Header", "order": 1, "description": "Navigation and main headline"},
                    {"name": "Hero", "order": 2, "description": "Main value proposition"},
                    {"name": "Features", "order": 3, "description": "Key features or benefits"},
                    {"name": "CallToAction", "order": 4, "description": "Call to action section"}
                ]
            }