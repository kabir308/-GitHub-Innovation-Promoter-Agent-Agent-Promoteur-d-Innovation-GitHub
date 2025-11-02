"""
Feedback collection module for innovative projects.
Collects and manages feedback from the community.
"""

import json
from datetime import datetime

class FeedbackCollector:
    """Collects and manages project feedback."""
    
    def __init__(self, storage_file="feedback_data.json"):
        self.storage_file = storage_file
        self.feedback = self._load_feedback()
    
    def _load_feedback(self):
        """Load existing feedback from storage."""
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_feedback(self):
        """Save feedback to storage."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.feedback, f, indent=2)
    
    def add_feedback(self, project_name, rating, comment, user="anonymous"):
        """
        Add feedback for a project.
        
        Args:
            project_name: Full name of the project
            rating: Rating from 1-5
            comment: Text feedback
            user: Username of the reviewer
        
        Returns:
            True if successful
        """
        if project_name not in self.feedback:
            self.feedback[project_name] = {
                "ratings": [],
                "comments": [],
                "average_rating": 0
            }
        
        feedback_entry = {
            "user": user,
            "rating": min(max(int(rating), 1), 5),  # Clamp between 1-5
            "comment": comment,
            "timestamp": datetime.now().isoformat()
        }
        
        self.feedback[project_name]["ratings"].append(feedback_entry["rating"])
        self.feedback[project_name]["comments"].append(feedback_entry)
        
        # Update average
        ratings = self.feedback[project_name]["ratings"]
        self.feedback[project_name]["average_rating"] = sum(ratings) / len(ratings)
        
        self._save_feedback()
        return True
    
    def get_feedback(self, project_name):
        """Get all feedback for a project."""
        return self.feedback.get(project_name, {})
    
    def get_top_rated_projects(self, limit=10):
        """Get top-rated projects."""
        projects = [(name, data["average_rating"]) 
                   for name, data in self.feedback.items() 
                   if data.get("average_rating", 0) > 0]
        projects.sort(key=lambda x: x[1], reverse=True)
        return projects[:limit]
    
    def get_project_stats(self, project_name):
        """Get statistics for a project."""
        if project_name not in self.feedback:
            return None
        
        data = self.feedback[project_name]
        return {
            "average_rating": data["average_rating"],
            "total_reviews": len(data["ratings"]),
            "rating_distribution": self._get_rating_distribution(data["ratings"])
        }
    
    def _get_rating_distribution(self, ratings):
        """Get distribution of ratings."""
        distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for rating in ratings:
            distribution[rating] = distribution.get(rating, 0) + 1
        return distribution

def collect_feedback_interactive(project):
    """Interactive feedback collection for a project."""
    collector = FeedbackCollector()
    
    print(f"\n📝 Feedback for: {project['full_name']}")
    print("Rate this project (1-5): ", end="")
    try:
        rating = int(input())
        print("Your comment: ", end="")
        comment = input()
        
        collector.add_feedback(project['full_name'], rating, comment)
        print("✅ Thank you for your feedback!")
        
    except (ValueError, KeyboardInterrupt):
        print("\n❌ Feedback cancelled")
