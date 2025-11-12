"""
Demo script for Landing Page Designer Agent - Works without API key
"""

import sys
import os
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from landing_page_designer.utils.file_manager import ComponentFileManager

class MockLLM:
    """Mock LLM for demonstration purposes"""
    
    def invoke(self, prompt):
        class MockResponse:
            def __init__(self, content):
                self.content = content
        
        if "planner" in prompt.lower() or "sections" in prompt.lower():
            return MockResponse('''{
    "sections": [
        {"name": "Header", "order": 1, "description": "Navigation and hero section"},
        {"name": "Features", "order": 2, "description": "Key product features"},
        {"name": "CallToAction", "order": 3, "description": "Sign up or contact section"}
    ]
}''')
        
        elif "design" in prompt.lower() and "architect" in prompt.lower():
            return MockResponse('''{
    "color_scheme": {
        "primary": "blue-600",
        "secondary": "gray-100",
        "accent": "green-500",
        "text": "gray-900"
    },
    "typography": {
        "heading": "text-4xl font-bold",
        "subheading": "text-xl font-semibold",
        "body": "text-base"
    },
    "spacing": {
        "section": "py-16",
        "container": "px-4 mx-auto max-w-6xl"
    }
}''')
        
        elif "Header" in prompt:
            return MockResponse('''import React from 'react';

const Header = () => {
  return (
    <header className="bg-white shadow-sm py-4">
      <div className="px-4 mx-auto max-w-6xl">
        <div className="flex justify-between items-center">
          <div className="text-2xl font-bold text-blue-600">
            MyApp
          </div>
          <nav className="hidden md:flex space-x-8">
            <a href="#features" className="text-gray-600 hover:text-blue-600">Features</a>
            <a href="#about" className="text-gray-600 hover:text-blue-600">About</a>
            <a href="#contact" className="text-gray-600 hover:text-blue-600">Contact</a>
          </nav>
          <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">
            Get Started
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;''')
        
        elif "Features" in prompt:
            return MockResponse('''import React from 'react';

const Features = () => {
  const features = [
    { title: "Fast & Reliable", description: "Built for speed and performance" },
    { title: "Easy to Use", description: "Intuitive interface for everyone" },
    { title: "24/7 Support", description: "Always here when you need us" }
  ];

  return (
    <section className="bg-gray-50 py-16">
      <div className="px-4 mx-auto max-w-6xl">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Amazing Features
          </h2>
          <p className="text-xl text-gray-600">
            Everything you need to succeed
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="text-center p-6 bg-white rounded-lg shadow-sm">
              <h3 className="text-xl font-semibold text-gray-900 mb-4">
                {feature.title}
              </h3>
              <p className="text-gray-600">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;''')
        
        elif "CallToAction" in prompt:
            return MockResponse('''import React from 'react';

const CallToAction = () => {
  return (
    <section className="bg-blue-600 py-16">
      <div className="px-4 mx-auto max-w-6xl">
        <div className="text-center">
          <h2 className="text-4xl font-bold text-white mb-4">
            Ready to Get Started?
          </h2>
          <p className="text-xl text-blue-100 mb-8">
            Join thousands of satisfied customers today
          </p>
          <div className="space-x-4">
            <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-50">
              Start Free Trial
            </button>
            <button className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700">
              Contact Sales
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CallToAction;''')
        
        elif "validation" in prompt.lower() or "approve" in prompt.lower():
            return MockResponse("APPROVED")
        
        else:
            return MockResponse("Default response")

def run_demo():
    """Run a complete demo without requiring API key"""
    print("🚀 Landing Page Designer Agent - DEMO MODE")
    print("=" * 50)
    print("📝 Demo Brief: Create a landing page for a SaaS productivity app")
    print("💡 Demo Inspiration: Modern, clean design with professional look")
    print("🏷️ Demo Site Name: saas-demo")
    
    # Initialize components with unique folder
    file_manager = ComponentFileManager("saas-demo")
    
    # Step 1: Planning
    print("\n🎯 Step 1: Planning sections...")
    sections = [
        {"name": "Header", "order": 1, "description": "Navigation and hero section"},
        {"name": "Features", "order": 2, "description": "Key product features"},
        {"name": "CallToAction", "order": 3, "description": "Sign up or contact section"}
    ]
    print(f"📋 Planned {len(sections)} sections")
    
    # Step 2: Design Architecture
    print("\n🎨 Step 2: Creating design configuration...")
    design_config = {
        "color_scheme": {
            "primary": "blue-600",
            "secondary": "gray-100",
            "accent": "green-500",
            "text": "gray-900"
        },
        "typography": {
            "heading": "text-4xl font-bold",
            "subheading": "text-xl font-semibold",
            "body": "text-base"
        },
        "spacing": {
            "section": "py-16",
            "container": "px-4 mx-auto max-w-6xl"
        }
    }
    print("🎨 Design configuration created")
    
    # Step 3: Component Search (pass-through)
    print("\n🔍 Step 3: Component search...")
    components_info = []
    for section in sections:
        component_info = {
            "name": section["name"],
            "description": section["description"],
            "design_config": design_config,
            "status": "ready_for_refactor"
        }
        components_info.append(component_info)
    print(f"🔍 Prepared {len(components_info)} components")
    
    # Step 4: Create Components (Simplified - No Validation Loop)
    print("\n🔧 Step 4: Creating components...")
    mock_llm = MockLLM()
    created_components = []
    
    for component_info in components_info:
        print(f"  🔧 Creating component: {component_info['name']}")
        
        # Mock refactor
        response = mock_llm.invoke(f"Create {component_info['name']} component")
        component_code = response.content
        
        print(f"  ✅ Component {component_info['name']} created successfully")
        
        # Create the actual file
        success = file_manager.create_component(component_info['name'], component_code)
        if success:
            created_components.append(component_info['name'])
    
    # Step 5: Finalize
    print(f"\n🎉 Step 5: Finalizing {len(created_components)} components...")
    file_manager.update_app_jsx(created_components)
    
    print("\n✅ Demo completed successfully!")
    print(f"📁 Created components: {', '.join(created_components)}")
    print(f"📄 Updated App.jsx with new components")
    print("\n🌐 To preview the landing page:")
    print("   cd output_react_project")
    print("   npm run dev")

if __name__ == "__main__":
    run_demo()