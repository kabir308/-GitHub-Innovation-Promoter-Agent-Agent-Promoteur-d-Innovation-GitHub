#!/usr/bin/env python3
"""
Quick test script to verify core functionality.
Run with: python test_functionality.py
"""

import sys
sys.path.insert(0, '.')

def test_detection():
    """Test project detection."""
    print("\n🧪 Testing project detection...")
    from modules import detect
    
    projects = detect.get_innovative_projects(limit=2)
    assert len(projects) > 0, "Should return at least one project"
    assert 'full_name' in projects[0], "Project should have full_name"
    assert 'innovation_score' in projects[0], "Project should have innovation_score"
    print("   ✅ Detection works")
    return projects

def test_promotion(projects):
    """Test project promotion."""
    print("\n🧪 Testing project promotion...")
    from modules import promote
    
    # Test console format
    promote.promote_project(projects[0], format="console")
    
    # Test JSON format
    json_output = promote.promote_project(projects[0], format="json")
    assert json_output is not None, "JSON output should not be None"
    
    # Test Markdown format
    md_output = promote.promote_project(projects[0], format="markdown")
    assert md_output is not None, "Markdown output should not be None"
    
    print("   ✅ Promotion works")

def test_ai_analysis(projects):
    """Test AI analysis."""
    print("\n🧪 Testing AI analysis...")
    from ai import advanced_analysis
    
    analysis = advanced_analysis.analyze_project_with_ai(projects[0])
    assert 'is_innovative' in analysis, "Analysis should include is_innovative"
    assert 'technologies' in analysis, "Analysis should include technologies"
    assert 'sentiment' in analysis, "Analysis should include sentiment"
    assert 'trending_score' in analysis, "Analysis should include trending_score"
    
    print(f"   Technologies detected: {', '.join(analysis['technologies']) if analysis['technologies'] else 'None'}")
    print(f"   Sentiment: {analysis['sentiment']['label']}")
    print(f"   Trending score: {analysis['trending_score']}/100")
    print("   ✅ AI analysis works")

def test_recommendations(projects):
    """Test recommendation engine."""
    print("\n🧪 Testing recommendations...")
    from modules import recommend
    
    # Test collaboration recommendations
    recs = recommend.recommend_collaborations(projects, user_interests=["ai", "python"], limit=3)
    assert isinstance(recs, list), "Recommendations should be a list"
    
    # Test opportunity suggestions
    if projects:
        opportunities = recommend.suggest_opportunities(projects[0])
        assert isinstance(opportunities, list), "Opportunities should be a list"
    
    print("   ✅ Recommendations work")

def test_network_analysis(projects):
    """Test network analysis."""
    print("\n🧪 Testing network analysis...")
    from modules import network_analysis
    
    ecosystem = network_analysis.analyze_ecosystem(projects)
    assert 'total_projects' in ecosystem, "Ecosystem should include total_projects"
    assert 'network_density' in ecosystem, "Ecosystem should include network_density"
    
    print(f"   Total projects: {ecosystem['total_projects']}")
    print(f"   Network density: {ecosystem['network_density']}")
    print("   ✅ Network analysis works")

def test_notifications(projects):
    """Test notification system."""
    print("\n🧪 Testing notifications...")
    from modules.notifications import NotificationManager
    
    notifier = NotificationManager()
    result = notifier.send_notification("new_project", projects[0], "Test notification")
    assert result == True, "Notification should be sent successfully"
    
    history = notifier.get_notification_history()
    assert len(history) > 0, "Should have notification history"
    
    print("   ✅ Notifications work")

def test_feedback():
    """Test feedback system."""
    print("\n🧪 Testing feedback system...")
    from modules.feedback import FeedbackCollector
    
    collector = FeedbackCollector("/tmp/test_feedback.json")
    result = collector.add_feedback("test/project", 5, "Great project!")
    assert result == True, "Feedback should be added successfully"
    
    stats = collector.get_project_stats("test/project")
    assert stats is not None, "Should return project stats"
    assert stats['average_rating'] == 5.0, "Average rating should be 5.0"
    
    print("   ✅ Feedback system works")

def test_multilingual():
    """Test multilingual support."""
    print("\n🧪 Testing multilingual support...")
    from modules.i18n import set_language, t, bilingual
    
    set_language("en")
    english_text = t("innovative_project")
    
    set_language("fr")
    french_text = t("innovative_project")
    
    assert english_text != french_text, "English and French should differ"
    
    bilingual_text = bilingual("innovative_project")
    assert "/" in bilingual_text, "Bilingual should contain both languages"
    
    print("   ✅ Multilingual support works")

def test_social_media(projects):
    """Test social media connectors."""
    print("\n🧪 Testing social media connectors...")
    from connectors import twitter, linkedin
    
    # Test Twitter
    tweet_result = twitter.publish_to_twitter(projects[0])
    assert tweet_result['status'] == 'success', "Twitter should return success"
    assert len(tweet_result['content']) <= 280, "Tweet should be under 280 characters"
    
    # Test LinkedIn
    linkedin_result = linkedin.publish_to_linkedin(projects[0])
    assert linkedin_result['status'] == 'success', "LinkedIn should return success"
    
    print("   ✅ Social media connectors work")

def main():
    """Run all tests."""
    print("="*70)
    print("🧪 GITHUB INNOVATION PROMOTER - FUNCTIONALITY TESTS")
    print("="*70)
    
    try:
        # Run tests in sequence
        projects = test_detection()
        test_promotion(projects)
        test_ai_analysis(projects)
        test_recommendations(projects)
        test_network_analysis(projects)
        test_notifications(projects)
        test_feedback()
        test_multilingual()
        test_social_media(projects)
        
        print("\n" + "="*70)
        print("✅ ALL TESTS PASSED!")
        print("="*70 + "\n")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
