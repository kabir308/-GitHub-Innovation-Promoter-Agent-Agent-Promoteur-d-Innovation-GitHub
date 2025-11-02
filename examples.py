#!/usr/bin/env python3
"""
Example usage script for GitHub Innovation Promoter.
Demonstrates various features and capabilities.
"""

import sys
sys.path.insert(0, '.')

from modules import detect, promote, recommend, feedback, notifications, network_analysis
from modules.i18n import set_language
from ai import advanced_analysis
from connectors import twitter, linkedin

def example_basic_usage():
    """Example 1: Basic project detection and promotion."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Usage")
    print("="*70 + "\n")
    
    # Detect projects
    projects = detect.get_innovative_projects(limit=3)
    
    # Promote each project
    for project in projects:
        promote.promote_project(project)

def example_ai_analysis():
    """Example 2: AI-powered project analysis."""
    print("\n" + "="*70)
    print("EXAMPLE 2: AI Analysis")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=1)
    
    if projects:
        project = projects[0]
        analysis = advanced_analysis.analyze_project_with_ai(project)
        
        print(f"Project: {project['full_name']}")
        print(f"\nAI Analysis Results:")
        print(f"  - Is Innovative: {analysis['is_innovative']}")
        print(f"  - Technologies: {', '.join(analysis['technologies'])}")
        print(f"  - Sentiment: {analysis['sentiment']['label']} (score: {analysis['sentiment']['score']})")
        print(f"  - Trending Score: {analysis['trending_score']}/100")
        print(f"  - Maturity Level: {analysis['maturity_level']}")
        print(f"  - Recommendation: {analysis['recommendation']}")

def example_recommendations():
    """Example 3: Getting personalized recommendations."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Personalized Recommendations")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=10)
    user_interests = ["ai", "machine learning", "python"]
    
    recommendations = recommend.recommend_collaborations(
        projects, 
        user_interests=user_interests,
        limit=3
    )
    
    print(f"Recommendations based on interests: {', '.join(user_interests)}\n")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['project']['full_name']}")
        print(f"   Relevance Score: {rec['relevance_score']}")
        print(f"   Reasons: {'; '.join(rec['reasons'])}")
        print()

def example_similar_projects():
    """Example 4: Finding similar projects."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Similar Projects")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=10)
    
    if projects:
        target = projects[0]
        print(f"Finding projects similar to: {target['full_name']}\n")
        
        similar = recommend.find_similar_projects(target, projects, limit=3)
        
        for sim in similar:
            print(f"  • {sim['project']['full_name']}")
            print(f"    Similarity Score: {sim['similarity_score']}")
            print()

def example_social_media():
    """Example 5: Social media promotion."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Social Media Promotion")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=1)
    
    if projects:
        project = projects[0]
        
        # Twitter
        print("\n--- Twitter ---")
        twitter.publish_to_twitter(project)
        
        print("\n--- Twitter Thread ---")
        thread = twitter.generate_thread(project)
        for i, tweet in enumerate(thread, 1):
            print(f"\nTweet {i}:")
            print(tweet)
        
        # LinkedIn
        print("\n--- LinkedIn ---")
        linkedin.publish_to_linkedin(project)

def example_notifications():
    """Example 6: Notification system."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Notifications")
    print("="*70 + "\n")
    
    notifier = notifications.NotificationManager()
    projects = detect.get_innovative_projects(limit=3)
    
    # Send different types of notifications
    for i, project in enumerate(projects):
        notification_types = ["new_project", "trending", "opportunity"]
        notifier.send_notification(notification_types[i % 3], project)
    
    # Show notification history
    print("\nNotification History:")
    history = notifier.get_notification_history()
    for notif in history:
        print(f"  [{notif['type']}] {notif['message']}")

def example_network_analysis():
    """Example 7: Network analysis."""
    print("\n" + "="*70)
    print("EXAMPLE 7: Network Analysis")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=15)
    
    # Analyze ecosystem
    ecosystem = network_analysis.analyze_ecosystem(projects)
    
    print("Ecosystem Analysis:")
    print(f"  Total Projects: {ecosystem['total_projects']}")
    print(f"  Total Connections: {ecosystem['total_connections']}")
    print(f"  Communities: {ecosystem['communities']}")
    print(f"  Network Density: {ecosystem['network_density']}")
    
    print("\nMost Central Projects:")
    for name, connections in ecosystem['central_projects']:
        print(f"  • {name}: {connections} connections")
    
    # Find collaborators for first project
    if projects:
        print(f"\nSuggested Collaborators for {projects[0]['full_name']}:")
        suggestions = network_analysis.suggest_collaborators(
            projects[0]['full_name'], 
            projects, 
            limit=3
        )
        for sug in suggestions:
            print(f"  • {sug['project']} (similarity: {sug['similarity']})")

def example_multilingual():
    """Example 8: Multilingual support."""
    print("\n" + "="*70)
    print("EXAMPLE 8: Multilingual Support")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=1)
    
    if projects:
        project = projects[0]
        
        # English
        set_language("en")
        print("--- English ---")
        promote.promote_project(project)
        
        # French
        set_language("fr")
        print("\n--- Français ---")
        promote.promote_project(project)

def example_different_formats():
    """Example 9: Different promotion formats."""
    print("\n" + "="*70)
    print("EXAMPLE 9: Multiple Output Formats")
    print("="*70 + "\n")
    
    projects = detect.get_innovative_projects(limit=1)
    
    if projects:
        project = projects[0]
        
        print("\n--- Console Format ---")
        promote.promote_project(project, format="console")
        
        print("\n--- JSON Format ---")
        json_output = promote.promote_project(project, format="json")
        if json_output:
            print(json_output)
        
        print("\n--- Markdown Format ---")
        md_output = promote.promote_project(project, format="markdown")
        if md_output:
            print(md_output)

def main():
    """Run all examples."""
    examples = [
        ("Basic Usage", example_basic_usage),
        ("AI Analysis", example_ai_analysis),
        ("Recommendations", example_recommendations),
        ("Similar Projects", example_similar_projects),
        ("Social Media", example_social_media),
        ("Notifications", example_notifications),
        ("Network Analysis", example_network_analysis),
        ("Multilingual", example_multilingual),
        ("Output Formats", example_different_formats)
    ]
    
    print("\n" + "="*70)
    print("GITHUB INNOVATION PROMOTER - EXAMPLES")
    print("="*70)
    print("\nAvailable Examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    print("  0. Run all examples")
    
    choice = input("\nSelect example (0-9): ").strip()
    
    if choice == "0":
        for name, func in examples:
            try:
                func()
            except Exception as e:
                print(f"\n❌ Error in {name}: {e}")
    elif choice.isdigit() and 1 <= int(choice) <= len(examples):
        name, func = examples[int(choice) - 1]
        try:
            func()
        except Exception as e:
            print(f"\n❌ Error: {e}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
