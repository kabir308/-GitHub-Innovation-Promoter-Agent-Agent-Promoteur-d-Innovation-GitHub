"""
Notification module for alerting users about projects and opportunities.
Supports multiple notification channels and user preferences.
"""

import json
from datetime import datetime

class NotificationManager:
    """Manages notifications for users."""
    
    def __init__(self, config_file="notifications_config.json"):
        self.config_file = config_file
        self.config = self._load_config()
        self.notification_history = []
    
    def _load_config(self):
        """Load notification configuration."""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "channels": {
                    "email": False,
                    "console": True,
                    "webhook": False
                },
                "preferences": {
                    "min_stars": 100,
                    "keywords": ["ai", "innovation"],
                    "languages": []
                }
            }
    
    def send_notification(self, notification_type, project, message=""):
        """
        Send a notification about a project.
        
        Args:
            notification_type: Type of notification (new_project, trending, opportunity)
            project: Project dictionary
            message: Custom message
        
        Returns:
            True if notification was sent
        """
        notification = {
            "type": notification_type,
            "project": project.get("full_name"),
            "message": message or self._generate_message(notification_type, project),
            "timestamp": datetime.now().isoformat(),
            "url": project.get("html_url")
        }
        
        self.notification_history.append(notification)
        
        # Send to enabled channels
        if self.config["channels"].get("console", True):
            self._send_console_notification(notification)
        
        if self.config["channels"].get("email", False):
            self._send_email_notification(notification)
        
        if self.config["channels"].get("webhook", False):
            self._send_webhook_notification(notification)
        
        return True
    
    def _generate_message(self, notification_type, project):
        """Generate notification message."""
        name = project.get("full_name")
        stars = project.get("stargazers_count", 0)
        
        messages = {
            "new_project": f"New innovative project discovered: {name} ({stars} ⭐)",
            "trending": f"Trending now: {name} is gaining popularity! ({stars} ⭐)",
            "opportunity": f"Contribution opportunity: {name} has open issues",
            "milestone": f"Milestone reached: {name} has reached {stars} stars!",
            "update": f"Update available for: {name}"
        }
        
        return messages.get(notification_type, f"Notification about {name}")
    
    def _send_console_notification(self, notification):
        """Send console notification."""
        icons = {
            "new_project": "🆕",
            "trending": "🔥",
            "opportunity": "💡",
            "milestone": "🎯",
            "update": "📢"
        }
        
        icon = icons.get(notification["type"], "📬")
        print(f"\n{icon} NOTIFICATION [{notification['timestamp']}]")
        print(f"   {notification['message']}")
        print(f"   🔗 {notification['url']}\n")
    
    def _send_email_notification(self, notification):
        """Send email notification (mock)."""
        # In production, integrate with email service
        print(f"📧 Email notification queued: {notification['message']}")
    
    def _send_webhook_notification(self, notification):
        """Send webhook notification (mock)."""
        # In production, send to webhook URL
        print(f"🔔 Webhook notification sent: {notification['message']}")
    
    def check_and_notify(self, project):
        """
        Check if project matches user preferences and send notification.
        
        Args:
            project: Project dictionary
        
        Returns:
            True if notification was sent
        """
        prefs = self.config.get("preferences", {})
        
        # Check minimum stars
        if project.get("stargazers_count", 0) < prefs.get("min_stars", 0):
            return False
        
        # Check keywords
        keywords = prefs.get("keywords", [])
        if keywords:
            text = f"{project.get('description', '')} {project.get('full_name', '')}".lower()
            if not any(keyword.lower() in text for keyword in keywords):
                return False
        
        # Check languages
        languages = prefs.get("languages", [])
        if languages and project.get("language") not in languages:
            return False
        
        # Send notification
        return self.send_notification("new_project", project)
    
    def get_notification_history(self, limit=10):
        """Get recent notifications."""
        return self.notification_history[-limit:]
    
    def configure_channel(self, channel, enabled):
        """Enable or disable a notification channel."""
        if channel in self.config["channels"]:
            self.config["channels"][channel] = enabled
            return True
        return False
    
    def set_preferences(self, **kwargs):
        """Set user notification preferences."""
        for key, value in kwargs.items():
            if key in self.config["preferences"]:
                self.config["preferences"][key] = value

def create_digest(projects, period="daily"):
    """
    Create a digest notification for multiple projects.
    
    Args:
        projects: List of projects
        period: Time period (daily, weekly)
    
    Returns:
        Formatted digest text
    """
    header = f"\n{'='*70}\n📊 {period.upper()} INNOVATION DIGEST\n{'='*70}\n"
    
    summary = f"\n🎯 Found {len(projects)} innovative projects\n\n"
    
    items = []
    for i, project in enumerate(projects[:10], 1):
        name = project.get("full_name", "")
        stars = project.get("stargazers_count", 0)
        desc = project.get("description", "No description")[:80]
        items.append(f"{i}. {name} ({stars} ⭐)\n   {desc}...")
    
    footer = f"\n{'='*70}\n"
    
    return header + summary + "\n\n".join(items) + footer

def notify_batch(manager, projects, notification_type="new_project"):
    """
    Send notifications for a batch of projects.
    
    Args:
        manager: NotificationManager instance
        projects: List of projects
        notification_type: Type of notification
    """
    for project in projects:
        manager.send_notification(notification_type, project)
