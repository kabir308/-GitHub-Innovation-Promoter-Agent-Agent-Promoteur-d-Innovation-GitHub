"""
Recommendation module for suggesting collaborations and opportunities.
Uses project similarity and user interests to recommend connections.
"""

def recommend_collaborations(projects, user_interests=None, limit=5):
    """
    Recommend collaboration opportunities based on projects.
    
    Args:
        projects: List of project dictionaries
        user_interests: List of keywords user is interested in
        limit: Maximum number of recommendations
    
    Returns:
        List of recommended projects with reasons
    """
    if user_interests is None:
        user_interests = ["ai", "machine learning", "innovation"]
    
    recommendations = []
    
    for project in projects:
        relevance_score = _calculate_relevance(project, user_interests)
        if relevance_score > 0:
            recommendations.append({
                "project": project,
                "relevance_score": relevance_score,
                "reasons": _get_recommendation_reasons(project, user_interests)
            })
    
    # Sort by relevance
    recommendations.sort(key=lambda x: x["relevance_score"], reverse=True)
    return recommendations[:limit]

def _calculate_relevance(project, interests):
    """Calculate how relevant a project is to user interests."""
    score = 0
    description = (project.get("description") or "").lower()
    name = project.get("full_name", "").lower()
    language = (project.get("language") or "").lower()
    
    for interest in interests:
        interest_lower = interest.lower()
        if interest_lower in description:
            score += 3
        if interest_lower in name:
            score += 2
        if interest_lower in language:
            score += 1
    
    # Boost for high-quality projects
    if project.get("stargazers_count", 0) > 1000:
        score += 2
    if project.get("forks_count", 0) > 100:
        score += 1
    
    return score

def _get_recommendation_reasons(project, interests):
    """Generate human-readable reasons for recommendation."""
    reasons = []
    description = (project.get("description") or "").lower()
    name = project.get("full_name", "").lower()
    
    matched_interests = [
        interest for interest in interests 
        if interest.lower() in description or interest.lower() in name
    ]
    
    if matched_interests:
        reasons.append(f"Matches your interests: {', '.join(matched_interests[:3])}")
    
    if project.get("stargazers_count", 0) > 1000:
        reasons.append("Highly popular project")
    
    if project.get("open_issues_count", 0) > 10:
        reasons.append("Active community with opportunities to contribute")
    
    if project.get("language"):
        reasons.append(f"Written in {project['language']}")
    
    return reasons if reasons else ["Recommended based on innovation criteria"]

def find_similar_projects(target_project, all_projects, limit=5):
    """
    Find projects similar to a target project.
    
    Args:
        target_project: Reference project dict
        all_projects: List of all projects to search
        limit: Maximum number of similar projects
    
    Returns:
        List of similar projects with similarity scores
    """
    similar = []
    target_lang = target_project.get("language", "").lower()
    target_desc = (target_project.get("description") or "").lower()
    target_words = set(target_desc.split())
    
    for project in all_projects:
        if project.get("full_name") == target_project.get("full_name"):
            continue  # Skip the target itself
        
        similarity = 0
        
        # Language match
        if project.get("language", "").lower() == target_lang:
            similarity += 3
        
        # Description similarity
        proj_desc = (project.get("description") or "").lower()
        proj_words = set(proj_desc.split())
        common_words = target_words & proj_words
        similarity += len(common_words) * 0.5
        
        # Similar popularity
        target_stars = target_project.get("stargazers_count", 0)
        proj_stars = project.get("stargazers_count", 0)
        if target_stars > 0 and proj_stars > 0:
            ratio = min(target_stars, proj_stars) / max(target_stars, proj_stars)
            similarity += ratio * 2
        
        if similarity > 0:
            similar.append({
                "project": project,
                "similarity_score": round(similarity, 2)
            })
    
    similar.sort(key=lambda x: x["similarity_score"], reverse=True)
    return similar[:limit]

def suggest_opportunities(project):
    """
    Suggest contribution opportunities for a project.
    
    Args:
        project: Project dictionary
    
    Returns:
        List of opportunity suggestions
    """
    opportunities = []
    
    open_issues = project.get("open_issues_count", 0)
    if open_issues > 0:
        opportunities.append({
            "type": "contribute",
            "title": "Help resolve issues",
            "description": f"This project has {open_issues} open issues where you can contribute",
            "priority": "high" if open_issues > 50 else "medium"
        })
    
    forks = project.get("forks_count", 0)
    if forks > 10:
        opportunities.append({
            "type": "fork",
            "title": "Fork and customize",
            "description": f"Join {forks} other developers who have forked this project",
            "priority": "medium"
        })
    
    watchers = project.get("watchers_count", 0)
    if watchers > 100:
        opportunities.append({
            "type": "watch",
            "title": "Stay updated",
            "description": "Watch this trending project to receive updates",
            "priority": "low"
        })
    
    # Check for documentation opportunities
    has_docs = project.get("has_wiki") or project.get("has_pages")
    if not has_docs:
        opportunities.append({
            "type": "document",
            "title": "Contribute documentation",
            "description": "Help improve this project by adding documentation",
            "priority": "medium"
        })
    
    return opportunities
