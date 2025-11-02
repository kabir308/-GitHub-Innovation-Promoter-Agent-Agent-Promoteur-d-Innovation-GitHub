import requests
import time

INNOVATION_KEYWORDS = [
    "ai", "machine learning", "blockchain", "innovant", "cloud", "edge", "quantum", 
    "decentralized", "sustainability", "innovation", "neural", "deep-learning"
]

INNOVATION_CRITERIA = {
    "min_stars": 10,
    "min_forks": 5,
    "has_description": True,
    "active_within_days": 365
}

def get_innovative_projects(limit=10, criteria=None):
    """
    Detect innovative projects on GitHub based on keywords and criteria.
    
    Args:
        limit: Maximum number of projects to return
        criteria: Optional custom criteria dict
    
    Returns:
        List of project dictionaries with metadata
    """
    if criteria is None:
        criteria = INNOVATION_CRITERIA
    
    GITHUB_API = "https://api.github.com/search/repositories"
    query = "+".join(INNOVATION_KEYWORDS[:5])  # Limit keywords to avoid rate limiting
    params = {
        "q": f"{query} stars:>{criteria.get('min_stars', 10)} in:name,description",
        "sort": "stars",
        "order": "desc",
        "per_page": min(limit, 100)
    }
    
    try:
        response = requests.get(GITHUB_API, params=params, timeout=10)
        
        # Handle rate limiting
        if response.status_code == 403:
            print("⚠️  Rate limit reached. Using cached/demo data.")
            return _get_demo_projects()[:limit]
        
        response.raise_for_status()
        data = response.json()
        projects = data.get("items", [])
        
        # Filter by criteria
        filtered = []
        for project in projects[:limit]:
            if _meets_criteria(project, criteria):
                # Enrich project data
                project["innovation_score"] = _calculate_innovation_score(project)
                filtered.append(project)
        
        return filtered[:limit]
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching projects: {e}")
        return _get_demo_projects()[:limit]

def _meets_criteria(project, criteria):
    """Check if a project meets the innovation criteria."""
    if criteria.get("has_description") and not project.get("description"):
        return False
    if project.get("stargazers_count", 0) < criteria.get("min_stars", 0):
        return False
    if project.get("forks_count", 0) < criteria.get("min_forks", 0):
        return False
    return True

def _calculate_innovation_score(project):
    """Calculate an innovation score based on project metrics."""
    stars = project.get("stargazers_count", 0)
    forks = project.get("forks_count", 0)
    watchers = project.get("watchers_count", 0)
    open_issues = project.get("open_issues_count", 0)
    
    # Simple scoring algorithm
    score = (stars * 0.4) + (forks * 0.3) + (watchers * 0.2) + (open_issues * 0.1)
    return round(score, 2)

def _get_demo_projects():
    """Return demo projects for testing/fallback."""
    return [
        {
            "full_name": "demo/innovative-ai-project",
            "description": "An innovative AI project for demonstration",
            "stargazers_count": 1000,
            "forks_count": 200,
            "watchers_count": 150,
            "open_issues_count": 50,
            "html_url": "https://github.com/demo/innovative-ai-project",
            "language": "Python",
            "innovation_score": 550.0
        }
    ]