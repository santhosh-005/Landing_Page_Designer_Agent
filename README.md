# Landing Page Designer Agent MVP v1.0

A multi-agent system for automatically designing and generating landing pages using LangGraph, Gemini API, and React with Tailwind CSS.

## Architecture

The system follows a multi-agent workflow:

1. **Planner Agent** - Decides what sections are needed and in what order
2. **Design Architect Agent** - Creates design configuration for the entire landing page  
3. **Component Search Agent** - Searches for components (currently pass-through)
4. **Refactor & Validation Loop** - Self-correcting loop that creates and validates each component

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   - Copy the `.env` file and add your Gemini API key:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

3. **Install React dependencies (if not already done):**
   ```bash
   cd output_react_project
   npm install
   ```

## Usage

1. **Run the Landing Page Designer Agent:**
   ```bash
   python landing_page_designer/main.py
   ```

2. **Follow the prompts:**
   - Provide your landing page brief
   - Add any inspiration or specific requirements

3. **View the generated components:**
   - Components are created in `output_react_project/src/components/`
   - App.jsx is automatically updated to include all components

4. **Preview the landing page:**
   ```bash
   cd output_react_project
   npm run dev
   ```

## Project Structure

```
landing_page_designer/
├── main.py                 # Entry point
├── agents/
│   ├── planner_agent.py           # Plans sections
│   ├── design_architect_agent.py  # Creates design config
│   ├── component_search_agent.py  # Component search (pass-through)
│   ├── refactor_agent.py         # Creates React components
│   ├── visual_validation_agent.py # Validates components
│   └── graph.py                  # LangGraph workflow
└── utils/
    └── file_manager.py           # File operations

output_react_project/
├── src/
│   ├── components/              # Generated components
│   ├── App.jsx                 # Updated automatically
│   └── main.jsx
└── package.json
```

## Features

- **Multi-agent workflow** with self-correction loops
- **Automatic React component generation** with Tailwind CSS
- **Design consistency** through unified design configuration
- **File management** with automatic App.jsx updates
- **Responsive design** with modern Tailwind CSS classes

## Current Limitations (MVP)

- Component search is pass-through (no vector database yet)
- Simple validation logic
- Basic error handling
- Limited design templates

## Next Steps

- Add vector database for component search
- Implement more sophisticated validation
- Add more design templates and styles
- Improve error handling and user experience
- Add component preview functionality