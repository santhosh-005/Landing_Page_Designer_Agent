"""
File Manager for handling React component creation and updates
"""

import os
import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime

class ComponentFileManager:
    """Manages file operations for React components"""
    
    def __init__(self, site_name: str = None):
        self.project_root = Path(os.getenv('PROJECT_ROOT', 'c:/Users/Santhoshkumar V/Desktop/DeepAgent_02'))
        self.react_project_path = self.project_root / "output_react_project"
        
        # Create unique folder name for this site generation
        if site_name:
            folder_name = f"{site_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        else:
            folder_name = f"site_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Clean folder name (remove spaces, special chars)
        folder_name = "".join(c for c in folder_name if c.isalnum() or c in ['_', '-']).lower()
        
        self.site_folder = self.react_project_path / "src" / "components" / folder_name
        self.components_path = self.site_folder
        self.src_path = self.react_project_path / "src"
        
        # Create unique site components directory
        self.components_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Created unique site folder: {folder_name}")
        
        # Store the folder name for imports
        self.site_folder_name = folder_name
        
    def create_component(self, component_name: str, component_code: str) -> bool:
        """Create a new React component file"""
        try:
            # Sanitize component_code: remove markdown fences and surrounding ```js/``` blocks
            code = component_code or ""
            # Remove any leading/trailing ``` and language tags (```jsx, ```javascript, etc.)
            # and trim whitespace
            import re
            # strip leading/trailing code fences
            code = re.sub(r"^\s*```(?:[a-zA-Z0-9_-]+)?\n", "", code)
            code = re.sub(r"\n```\s*$", "", code)
            # If the code contains multiple duplicated import React lines, keep only one
            code_lines = code.splitlines()
            seen_import_react = False
            cleaned_lines = []
            for line in code_lines:
                stripped = line.strip()
                if stripped == "import React from 'react';" or stripped == 'import React from \"react\";':
                    if seen_import_react:
                        # skip duplicate
                        continue
                    seen_import_react = True
                cleaned_lines.append(line)
            code = "\n".join(cleaned_lines).strip() + "\n"

            component_file = self.components_path / f"{component_name}.jsx"
            with open(component_file, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"📄 Created component: {component_name}.jsx")
            return True
        except Exception as e:
            print(f"❌ Error creating component {component_name}: {str(e)}")
            return False
    
    def update_app_jsx(self, components: List[str]) -> bool:
        """Update App.jsx to include all created components"""
        try:
            app_jsx_path = self.src_path / "App.jsx"
            
            # Generate imports from the unique site folder
            imports = "\n".join([
                f"import {comp} from './components/{self.site_folder_name}/{comp}.jsx';" 
                for comp in components
            ])
            
            # Generate component usage
            component_usage = "\n      ".join([f"<{comp} />" for comp in components])
            
            # Create new App.jsx content
            app_content = f"""import React from 'react';
{imports}
import './index.css';

function App() {{
  return (
    <div className="min-h-screen">
      {component_usage}
    </div>
  );
}}

export default App;
"""
            
            with open(app_jsx_path, 'w', encoding='utf-8') as f:
                f.write(app_content)
            
            print("📄 Updated App.jsx with new components")
            return True
            
        except Exception as e:
            print(f"❌ Error updating App.jsx: {str(e)}")
            return False
    
    def read_existing_components(self) -> List[str]:
        """Read existing components in the components directory"""
        try:
            if not self.components_path.exists():
                return []
            
            components = []
            for file in self.components_path.glob("*.jsx"):
                components.append(file.stem)
            
            return components
        except Exception as e:
            print(f"❌ Error reading existing components: {str(e)}")
            return []