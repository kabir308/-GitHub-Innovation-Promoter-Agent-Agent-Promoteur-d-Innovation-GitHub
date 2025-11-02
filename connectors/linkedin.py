"""
LinkedIn connector for sharing innovative projects.
Provides functionality to post project updates to LinkedIn.
"""

def publish_to_linkedin(project):
    """
    Publish project to LinkedIn (mock implementation).
    
    In a production environment, this would use the LinkedIn API
    with proper authentication and OAuth tokens.
    
    Args:
        project: Project dictionary
    
    Returns:
        Success message
    """
    post_text = _generate_linkedin_post(project)
    
    # Mock posting - in production, use LinkedIn API
    print(f"\n📱 LinkedIn Post (mock):")
    print("=" * 70)
    print(post_text)
    print("=" * 70)
    
    return {
        "status": "success",
        "platform": "LinkedIn",
        "message": "Post would be published to LinkedIn",
        "content": post_text
    }

def _generate_linkedin_post(project):
    """Generate LinkedIn-formatted post text."""
    name = project.get("full_name", "Unknown Project")
    description = project.get("description", "An innovative project")
    url = project.get("html_url", "")
    stars = project.get("stargazers_count", 0)
    language = project.get("language", "")
    
    # Professional LinkedIn-style post
    post = f"""🚀 Exciting Innovation Alert! 

I came across an innovative project that I wanted to share with my network:

📦 {name}

{description}

Key Highlights:
⭐ {stars} stars from the community
💻 Built with {language if language else 'cutting-edge technology'}
🔗 Check it out: {url}

This project demonstrates innovation in action. Perfect for developers and tech enthusiasts interested in the latest developments!

#Innovation #Technology #OpenSource #GitHub #TechCommunity"""

    if project.get("innovation_score"):
        post += f"\n\n🎯 Innovation Score: {project['innovation_score']}"
    
    return post

def share_multiple_projects(projects, limit=5):
    """
    Create a summary post for multiple projects.
    
    Args:
        projects: List of project dictionaries
        limit: Maximum projects to include
    
    Returns:
        LinkedIn post text
    """
    post_header = """🌟 Top Innovative GitHub Projects This Week!

I've been tracking some exciting innovations on GitHub. Here are my top picks:

"""
    
    project_items = []
    for i, project in enumerate(projects[:limit], 1):
        name = project.get("full_name", "")
        desc = project.get("description", "")[:100]  # Truncate
        url = project.get("html_url", "")
        
        project_items.append(f"{i}. {name}\n   {desc}...\n   {url}")
    
    footer = """

These projects showcase creativity, innovation, and the power of open-source collaboration!

#GitHub #Innovation #OpenSource #Technology #Development"""
    
    return post_header + "\n\n".join(project_items) + footer

def format_for_company_page(project, company_name="Your Company"):
    """
    Format project for company LinkedIn page.
    
    Args:
        project: Project dictionary
        company_name: Name of the company
    
    Returns:
        Company page formatted post
    """
    return f"""At {company_name}, we're committed to innovation and supporting the developer community.

Today, we're highlighting: {project.get('full_name')}

{project.get('description', 'An innovative open-source project')}

Why we think this matters:
• Addresses real-world challenges
• Active community engagement ({project.get('stargazers_count', 0)} stars)
• Open-source collaboration at its best

Explore the project: {project.get('html_url', '')}

#Innovation #OpenSource #TechLeadership #DeveloperCommunity"""
