"""
Streamlit dashboard application.
Run with: streamlit run dashboard_app.py
"""

import sys
sys.path.insert(0, '.')

from dashboard.web import show_dashboard
from modules import detect
import json

def load_config():
    """Load configuration."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"detection": {"limit": 20}}

def main():
    """Main dashboard application."""
    config = load_config()
    
    # Fetch projects
    limit = config.get("detection", {}).get("limit", 20)
    criteria = config.get("detection", {}).get("criteria")
    
    projects = detect.get_innovative_projects(limit=limit, criteria=criteria)
    
    # Show dashboard
    show_dashboard(projects)

if __name__ == "__main__":
    main()
