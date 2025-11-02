"""
Main GitHub Innovation Promoter Agent.
Orchestrates all modules to detect, analyze, and promote innovative projects.
"""

import json
import sys
from modules import detect, promote, recommend, feedback, notifications, network_analysis
from modules.i18n import t, set_language, bilingual
from ai import advanced_analysis
from connectors import twitter, linkedin

def load_config():
    """Load configuration from config.json."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return default config
        return {
            "detection": {"limit": 10},
            "language": "en",
            "promotion": {"default_format": "console"}
        }

def main():
    """Main agent execution."""
    config = load_config()
    
    # Set language from config
    set_language(config.get("language", "en"))
    
    print(f"\n{'='*70}")
    print(f"🌟 {bilingual('app_title')}")
    print(f"{'='*70}\n")
    print(f"{t('starting')}\n")
    
    # Detect innovative projects
    print("🔍 Detecting innovative projects...")
    limit = config.get("detection", {}).get("limit", 10)
    criteria = config.get("detection", {}).get("criteria")
    
    projects = detect.get_innovative_projects(limit=limit, criteria=criteria)
    
    if not projects:
        print(f"❌ {t('no_projects')}")
        return
    
    print(f"✅ {len(projects)} {t('projects_found')}\n")
    
    # Initialize notification manager
    notifier = notifications.NotificationManager()
    
    # Process each project
    for i, project in enumerate(projects, 1):
        print(f"\n--- Project {i}/{len(projects)} ---")
        
        # Promote project
        promote.promote_project(project, format=config.get("promotion", {}).get("default_format", "console"))
        
        # AI Analysis
        print("🤖 AI Analysis:")
        analysis = advanced_analysis.analyze_project_with_ai(project)
        print(f"   • Is Innovative: {analysis['is_innovative']}")
        print(f"   • Technologies: {', '.join(analysis['technologies']) if analysis['technologies'] else 'General'}")
        print(f"   • Sentiment: {analysis['sentiment']['label']}")
        print(f"   • Trending Score: {analysis['trending_score']}/100")
        print(f"   • Maturity: {analysis['maturity_level']}")
        print(f"   • Recommendation: {analysis['recommendation']}")
        
        # Check for opportunities
        print("\n💡 Opportunities:")
        opportunities = recommend.suggest_opportunities(project)
        for opp in opportunities[:3]:
            print(f"   • [{opp['priority'].upper()}] {opp['title']}: {opp['description']}")
        
        # Send notification if matches criteria
        if notifier.check_and_notify(project):
            print("   ✓ Notification sent")
    
    print(f"\n{'='*70}")
    print("📊 Summary & Recommendations")
    print(f"{'='*70}\n")
    
    # Get recommendations
    user_interests = config.get("recommendations", {}).get("user_interests", ["ai", "innovation"])
    recommendations = recommend.recommend_collaborations(
        projects, 
        user_interests=user_interests,
        limit=5
    )
    
    print(f"🎯 Top {len(recommendations)} Recommended Projects:")
    for rec in recommendations:
        print(f"\n   {rec['project']['full_name']}")
        print(f"   Relevance Score: {rec['relevance_score']}")
        print(f"   Reasons: {', '.join(rec['reasons'][:2])}")
    
    # Network analysis
    print(f"\n{'='*70}")
    print("🌐 Network Analysis")
    print(f"{'='*70}\n")
    
    ecosystem = network_analysis.analyze_ecosystem(projects)
    print(f"Total Projects: {ecosystem['total_projects']}")
    print(f"Total Connections: {ecosystem['total_connections']}")
    print(f"Communities Detected: {ecosystem['communities']}")
    print(f"Network Density: {ecosystem['network_density']}")
    
    print("\nMost Central Projects:")
    for name, connections in ecosystem['central_projects'][:5]:
        print(f"   • {name}: {connections} connections")
    
    # Social media promotion
    print(f"\n{'='*70}")
    print("📱 Social Media Promotion")
    print(f"{'='*70}\n")
    
    if projects and config.get("promotion", {}).get("enabled_platforms"):
        top_project = projects[0]
        
        if "twitter" in config["promotion"]["enabled_platforms"]:
            twitter.publish_to_twitter(top_project)
        
        if "linkedin" in config["promotion"]["enabled_platforms"]:
            linkedin.publish_to_linkedin(top_project)
    
    print(f"\n{'='*70}")
    print("✅ Agent execution completed successfully!")
    print(f"{'='*70}\n")
    
    # Offer to launch dashboard
    print("💡 Tip: Run 'streamlit run dashboard_app.py' to view the interactive dashboard")

def run_interactive_mode():
    """Run agent in interactive mode with menu."""
    while True:
        print("\n" + "="*70)
        print("🌟 GitHub Innovation Promoter - Interactive Mode")
        print("="*70)
        print("\n1. Detect and promote projects")
        print("2. Analyze specific project")
        print("3. Get recommendations")
        print("4. View network analysis")
        print("5. Launch dashboard")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            main()
        elif choice == "2":
            project_name = input("Enter project name (owner/repo): ").strip()
            # Implementation would fetch and analyze specific project
            print(f"Analysis for {project_name} would be shown here")
        elif choice == "3":
            print("Generating recommendations...")
            main()
        elif choice == "4":
            print("Running network analysis...")
            main()
        elif choice == "5":
            print("Launching dashboard...")
            print("Run: streamlit run dashboard_app.py")
            break
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    # Check for interactive mode flag
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive_mode()
    else:
        main()
