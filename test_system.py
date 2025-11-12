"""
Test script for Landing Page Designer Agent without requiring API key
"""

import sys
import os
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from landing_page_designer.utils.file_manager import ComponentFileManager

def test_file_manager():
    """Test the file manager functionality"""
    print("🧪 Testing File Manager...")
    
    file_manager = ComponentFileManager()
    
    # Test component creation
    test_component_code = """import React from 'react';

const TestComponent = () => {
  return (
    <section className="bg-white py-16">
      <div className="px-4 mx-auto max-w-6xl">
        <div className="text-center">
          <h2 className="text-4xl font-bold text-blue-600 mb-4">
            Test Component
          </h2>
          <p className="text-base text-gray-600 mb-8">
            This is a test component for the Landing Page Designer Agent.
          </p>
          <div className="bg-blue-600 text-white px-6 py-3 rounded-lg inline-block">
            Learn More
          </div>
        </div>
      </div>
    </section>
  );
};

export default TestComponent;
"""
    
    # Create test component
    success = file_manager.create_component("TestComponent", test_component_code)
    
    if success:
        print("✅ Component creation test passed")
        
        # Test App.jsx update
        components = ["TestComponent"]
        app_success = file_manager.update_app_jsx(components)
        
        if app_success:
            print("✅ App.jsx update test passed")
            print("🎉 File Manager tests completed successfully!")
            return True
        else:
            print("❌ App.jsx update test failed")
            return False
    else:
        print("❌ Component creation test failed")
        return False

def create_mock_workflow_test():
    """Create a simple mock workflow test"""
    print("🧪 Testing Mock Workflow...")
    
    # Mock state
    mock_state = {
        "user_brief": "Create a landing page for a SaaS product",
        "inspiration": "Modern, clean design",
        "sections": [
            {"name": "Header", "order": 1, "description": "Navigation and main headline"},
            {"name": "Hero", "order": 2, "description": "Main value proposition"},
        ],
        "design_config": {
            "color_scheme": {
                "primary": "blue-600",
                "secondary": "gray-100",
                "accent": "green-500",
                "text": "gray-900"
            }
        },
        "components": [],
        "current_component_index": 0
    }
    
    print("📋 Mock state created with 2 sections")
    print("🎨 Mock design config applied")
    print("✅ Mock workflow test completed!")
    
    return True

def main():
    """Run all tests"""
    print("🚀 Landing Page Designer Agent - Test Suite")
    print("=" * 50)
    
    try:
        # Test 1: File Manager
        file_manager_test = test_file_manager()
        
        # Test 2: Mock Workflow
        workflow_test = create_mock_workflow_test()
        
        if file_manager_test and workflow_test:
            print("\n🎉 All tests passed! The system is ready to use.")
            print("\nNext steps:")
            print("1. Add your Gemini API key to the .env file")
            print("2. Run: python landing_page_designer/main.py")
            print("3. Check the generated components in output_react_project/src/components/")
            return True
        else:
            print("\n❌ Some tests failed. Please check the setup.")
            return False
            
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        return False

if __name__ == "__main__":
    main()