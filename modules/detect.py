import requests

INNOVATION_KEYWORDS = [
    "ai", "machine learning", "blockchain", "innovant", "cloud", "edge", "quantum", "decentralized", "sustainability"
]

def get_innovative_projects():
    GITHUB_API = "https://api.github.com/search/repositories"
    query = "+".join(INNOVATION_KEYWORDS)
    params = {
        "q": f"{query} in:name,description",
        "sort": "stars",
        "order": "desc"
    }
    response = requests.get(GITHUB_API, params=params)
    return response.json().get("items", [])[:10]