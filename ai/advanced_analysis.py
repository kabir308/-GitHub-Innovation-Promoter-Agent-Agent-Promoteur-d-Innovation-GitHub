"""
Advanced AI/ML analysis for project evaluation.
Includes sentiment analysis, technology detection, and trend prediction.
"""

import re
from collections import Counter

# Technology keywords database
TECH_CATEGORIES = {
    "AI/ML": ["ai", "artificial intelligence", "machine learning", "deep learning", 
              "neural network", "tensorflow", "pytorch", "keras", "scikit-learn"],
    "Blockchain": ["blockchain", "cryptocurrency", "bitcoin", "ethereum", "smart contract",
                   "web3", "defi", "nft"],
    "Cloud": ["cloud", "aws", "azure", "gcp", "kubernetes", "docker", "serverless"],
    "Web": ["web", "frontend", "backend", "react", "vue", "angular", "node.js", "django"],
    "Mobile": ["mobile", "android", "ios", "react native", "flutter", "swift", "kotlin"],
    "Data": ["data science", "analytics", "big data", "data visualization", "pandas", "numpy"],
    "Security": ["security", "encryption", "authentication", "cybersecurity", "penetration"],
    "IoT": ["iot", "internet of things", "embedded", "arduino", "raspberry pi"],
    "DevOps": ["devops", "ci/cd", "jenkins", "github actions", "terraform", "ansible"]
}

def analyze_project_with_ai(project):
    """
    Comprehensive AI analysis of a project.
    
    Args:
        project: Project dictionary
    
    Returns:
        Analysis dictionary with insights
    """
    description = project.get("description", "")
    name = project.get("full_name", "")
    
    return {
        "is_innovative": _assess_innovation(project),
        "technologies": detect_technologies(project),
        "sentiment": analyze_sentiment(description),
        "trending_score": calculate_trending_score(project),
        "maturity_level": assess_maturity(project),
        "recommendation": generate_recommendation(project)
    }

def _assess_innovation(project):
    """Determine if project is truly innovative."""
    innovation_keywords = [
        "innovative", "novel", "breakthrough", "cutting-edge", "revolutionary",
        "next-generation", "advanced", "pioneering", "state-of-the-art"
    ]
    
    text = f"{project.get('description', '')} {project.get('full_name', '')}".lower()
    
    # Check for innovation keywords
    keyword_matches = sum(1 for keyword in innovation_keywords if keyword in text)
    
    # Check for modern technologies
    tech_count = len(detect_technologies(project))
    
    # Check for activity and community
    stars = project.get("stargazers_count", 0)
    forks = project.get("forks_count", 0)
    
    # Simple scoring
    score = (keyword_matches * 2) + tech_count + (1 if stars > 100 else 0) + (1 if forks > 20 else 0)
    
    return score >= 3

def detect_technologies(project):
    """
    Detect technologies used in the project.
    
    Returns:
        List of detected technology categories
    """
    text = f"{project.get('description', '')} {project.get('full_name', '')} {project.get('language', '')}".lower()
    
    detected = []
    for category, keywords in TECH_CATEGORIES.items():
        if any(keyword in text for keyword in keywords):
            detected.append(category)
    
    return detected

def analyze_sentiment(text):
    """
    Simple sentiment analysis of project description.
    
    Returns:
        Sentiment score and label (positive/neutral/negative)
    """
    if not text:
        return {"score": 0, "label": "neutral"}
    
    positive_words = [
        "excellent", "amazing", "great", "awesome", "innovative", "powerful",
        "efficient", "easy", "simple", "fast", "best", "modern", "advanced"
    ]
    
    negative_words = [
        "difficult", "complex", "slow", "deprecated", "broken", "outdated",
        "unstable", "experimental", "unmaintained"
    ]
    
    text_lower = text.lower()
    words = re.findall(r'\w+', text_lower)
    
    positive_count = sum(1 for word in positive_words if word in words)
    negative_count = sum(1 for word in negative_words if word in words)
    
    score = positive_count - negative_count
    
    if score > 2:
        label = "very positive"
    elif score > 0:
        label = "positive"
    elif score < -2:
        label = "negative"
    elif score < 0:
        label = "slightly negative"
    else:
        label = "neutral"
    
    return {"score": score, "label": label}

def calculate_trending_score(project):
    """
    Calculate trending score based on recent activity.
    
    Returns:
        Float score (0-100)
    """
    stars = project.get("stargazers_count", 0)
    forks = project.get("forks_count", 0)
    watchers = project.get("watchers_count", 0)
    open_issues = project.get("open_issues_count", 0)
    
    # Weighted combination
    score = (
        (stars * 0.4) +
        (forks * 0.3) +
        (watchers * 0.2) +
        (min(open_issues, 100) * 0.1)
    )
    
    # Normalize to 0-100
    normalized = min(100, score / 10)
    return round(normalized, 2)

def assess_maturity(project):
    """
    Assess project maturity level.
    
    Returns:
        String: experimental/alpha/beta/stable/mature
    """
    stars = project.get("stargazers_count", 0)
    forks = project.get("forks_count", 0)
    has_license = project.get("license") is not None
    
    if stars > 1000 and forks > 200 and has_license:
        return "mature"
    elif stars > 500 and forks > 50:
        return "stable"
    elif stars > 100 and forks > 20:
        return "beta"
    elif stars > 10:
        return "alpha"
    else:
        return "experimental"

def generate_recommendation(project):
    """
    Generate AI-based recommendation text.
    
    Returns:
        String recommendation
    """
    analysis = {
        "tech": detect_technologies(project),
        "trending": calculate_trending_score(project),
        "maturity": assess_maturity(project)
    }
    
    recommendations = []
    
    if analysis["trending"] > 70:
        recommendations.append("🔥 This is a hot trending project worth exploring!")
    
    if analysis["maturity"] in ["stable", "mature"]:
        recommendations.append("✅ Production-ready and well-maintained")
    elif analysis["maturity"] == "experimental":
        recommendations.append("🧪 Experimental - use with caution")
    
    if len(analysis["tech"]) >= 3:
        recommendations.append(f"🔧 Multi-technology stack: {', '.join(analysis['tech'][:3])}")
    
    if not recommendations:
        recommendations.append("📚 Interesting project to explore")
    
    return " | ".join(recommendations)

def extract_keywords(text, top_n=10):
    """
    Extract top keywords from text.
    
    Returns:
        List of (keyword, frequency) tuples
    """
    if not text:
        return []
    
    # Remove common words
    stop_words = set([
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "as", "is", "was", "are", "be", "this", "that"
    ])
    
    words = re.findall(r'\w+', text.lower())
    words = [w for w in words if w not in stop_words and len(w) > 3]
    
    counter = Counter(words)
    return counter.most_common(top_n)
