"""
Twitter connector for sharing innovative projects.
Provides functionality to post project updates to Twitter/X.
"""

def publish_to_twitter(project):
    """
    Publish project to Twitter (mock implementation).
    
    In a production environment, this would use the Twitter API
    with proper authentication and OAuth tokens.
    
    Args:
        project: Project dictionary
    
    Returns:
        Success message with tweet preview
    """
    tweet = _generate_tweet(project)
    
    # Mock posting
    print(f"\n🐦 Tweet (mock):")
    print("=" * 70)
    print(tweet)
    print("=" * 70)
    print(f"Character count: {len(tweet)}/280")
    
    return {
        "status": "success",
        "platform": "Twitter",
        "message": "Tweet would be posted",
        "content": tweet,
        "length": len(tweet)
    }

def _generate_tweet(project):
    """Generate a tweet for a project (max 280 chars)."""
    name = project.get("full_name", "")
    url = project.get("html_url", "")
    stars = project.get("stargazers_count", 0)
    
    # Create short tweet
    tweet = f"🚀 Discover {name}\n⭐ {stars} stars\n{url}\n\n#Innovation #GitHub #OpenSource #Tech"
    
    # Ensure it's under 280 characters
    if len(tweet) > 280:
        # Truncate the name if needed
        max_name_len = 280 - len(tweet) + len(name) - 10
        name_short = name[:max_name_len] + "..."
        tweet = f"🚀 {name_short}\n⭐ {stars} stars\n{url}\n#Innovation #GitHub"
    
    return tweet

def generate_thread(project):
    """
    Generate a Twitter thread for a project.
    
    Args:
        project: Project dictionary
    
    Returns:
        List of tweets forming a thread
    """
    thread = []
    
    # Tweet 1: Introduction
    name = project.get("full_name", "")
    thread.append(f"🧵 Thread: Exploring {name}\n\nA deep dive into this innovative project. 1/5 🚀")
    
    # Tweet 2: Description
    desc = project.get("description", "An innovative project")
    if len(desc) > 250:
        desc = desc[:247] + "..."
    thread.append(f"2/5 📝 What is it?\n\n{desc}")
    
    # Tweet 3: Stats
    stars = project.get("stargazers_count", 0)
    forks = project.get("forks_count", 0)
    language = project.get("language", "Multiple")
    thread.append(f"3/5 📊 By the numbers:\n⭐ {stars} stars\n🍴 {forks} forks\n💻 {language}")
    
    # Tweet 4: Innovation
    innovation_score = project.get("innovation_score", "N/A")
    thread.append(f"4/5 🎯 Innovation Score: {innovation_score}\n\nThis project stands out for its approach to solving real problems with modern tech.")
    
    # Tweet 5: CTA
    url = project.get("html_url", "")
    thread.append(f"5/5 🔗 Ready to explore?\n\n{url}\n\nStar it, fork it, contribute!\n\n#OpenSource #Innovation #GitHub")
    
    return thread

def create_hashtags(project):
    """
    Generate relevant hashtags for a project.
    
    Args:
        project: Project dictionary
    
    Returns:
        String of hashtags
    """
    hashtags = ["#Innovation", "#GitHub", "#OpenSource"]
    
    language = project.get("language")
    if language:
        hashtags.append(f"#{language.replace(' ', '')}")
    
    # Add tech-specific tags
    description = (project.get("description") or "").lower()
    tech_tags = {
        "ai": "#AI", "machine learning": "#MachineLearning",
        "blockchain": "#Blockchain", "web3": "#Web3",
        "cloud": "#Cloud", "devops": "#DevOps",
        "mobile": "#Mobile", "web": "#WebDev"
    }
    
    for keyword, tag in tech_tags.items():
        if keyword in description and tag not in hashtags:
            hashtags.append(tag)
            if len(hashtags) >= 8:  # Limit hashtags
                break
    
    return " ".join(hashtags)

def schedule_tweets(projects, interval_hours=4):
    """
    Schedule tweets for multiple projects.
    
    Args:
        projects: List of projects
        interval_hours: Hours between tweets
    
    Returns:
        Schedule plan
    """
    schedule = []
    
    for i, project in enumerate(projects):
        hours_offset = i * interval_hours
        schedule.append({
            "offset_hours": hours_offset,
            "project": project.get("full_name"),
            "tweet": _generate_tweet(project)
        })
    
    return schedule
