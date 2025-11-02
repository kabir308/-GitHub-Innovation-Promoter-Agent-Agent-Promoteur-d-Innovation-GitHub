"""
Multilingual support module.
Provides translations for English and French.
"""

TRANSLATIONS = {
    "en": {
        "app_title": "🌟 GitHub Innovation Promoter Agent",
        "innovative_project": "🚀 Innovative Project",
        "description": "Description",
        "stars": "Stars",
        "forks": "Forks",
        "watchers": "Watchers",
        "open_issues": "Open Issues",
        "language": "Language",
        "innovation_score": "Innovation Score",
        "link": "Link",
        "badge": "Badge",
        "starting": "Innovation Promoter Agent starting...",
        "projects_found": "projects found",
        "no_projects": "No projects found",
        "error_fetching": "Error fetching projects",
        "rate_limit": "Rate limit reached. Using cached data.",
        "notification": "NOTIFICATION",
        "trending_now": "Trending now",
        "new_project": "New innovative project discovered",
        "opportunity": "Contribution opportunity",
        "recommendations": "Personalized Recommendations",
        "analytics": "Analytics Dashboard",
        "trends": "Trends & Insights",
        "feedback": "Feedback",
        "thank_you": "Thank you for your feedback!",
        "rating": "Rating",
        "comment": "Comment",
        "submit": "Submit",
        "cancel": "Cancel",
        "view_on_github": "View on GitHub",
        "explore": "Explore",
        "total_projects": "Total Projects",
        "average_score": "Average Innovation Score",
        "sort_by": "Sort by",
        "filter": "Filter",
        "languages": "Languages",
        "minimum_stars": "Minimum Stars",
        "network_analysis": "Network Analysis",
        "communities": "Communities",
        "connections": "Connections",
        "collaboration_potential": "Collaboration Potential",
        "similar_projects": "Similar Projects",
        "suggested_opportunities": "Suggested Opportunities"
    },
    "fr": {
        "app_title": "🌟 Agent Promoteur d'Innovation GitHub",
        "innovative_project": "🚀 Projet Innovant",
        "description": "Description",
        "stars": "Étoiles",
        "forks": "Forks",
        "watchers": "Observateurs",
        "open_issues": "Issues Ouvertes",
        "language": "Langage",
        "innovation_score": "Score d'Innovation",
        "link": "Lien",
        "badge": "Badge",
        "starting": "Agent Promoteur d'Innovation démarre...",
        "projects_found": "projets trouvés",
        "no_projects": "Aucun projet trouvé",
        "error_fetching": "Erreur lors de la récupération des projets",
        "rate_limit": "Limite de taux atteinte. Utilisation de données en cache.",
        "notification": "NOTIFICATION",
        "trending_now": "Tendance actuellement",
        "new_project": "Nouveau projet innovant découvert",
        "opportunity": "Opportunité de contribution",
        "recommendations": "Recommandations Personnalisées",
        "analytics": "Tableau de Bord Analytique",
        "trends": "Tendances et Insights",
        "feedback": "Retour d'expérience",
        "thank_you": "Merci pour votre retour!",
        "rating": "Note",
        "comment": "Commentaire",
        "submit": "Soumettre",
        "cancel": "Annuler",
        "view_on_github": "Voir sur GitHub",
        "explore": "Explorer",
        "total_projects": "Total des Projets",
        "average_score": "Score d'Innovation Moyen",
        "sort_by": "Trier par",
        "filter": "Filtrer",
        "languages": "Langages",
        "minimum_stars": "Étoiles Minimum",
        "network_analysis": "Analyse de Réseau",
        "communities": "Communautés",
        "connections": "Connexions",
        "collaboration_potential": "Potentiel de Collaboration",
        "similar_projects": "Projets Similaires",
        "suggested_opportunities": "Opportunités Suggérées"
    }
}

class I18n:
    """Internationalization helper."""
    
    def __init__(self, language="en"):
        """
        Initialize with a language.
        
        Args:
            language: Language code (en, fr)
        """
        self.language = language if language in TRANSLATIONS else "en"
    
    def t(self, key):
        """
        Translate a key.
        
        Args:
            key: Translation key
        
        Returns:
            Translated string
        """
        return TRANSLATIONS[self.language].get(key, key)
    
    def set_language(self, language):
        """Change the current language."""
        if language in TRANSLATIONS:
            self.language = language
            return True
        return False
    
    def get_language(self):
        """Get current language."""
        return self.language
    
    def get_available_languages(self):
        """Get list of available languages."""
        return list(TRANSLATIONS.keys())

# Global instance
_i18n = I18n()

def t(key, language=None):
    """
    Quick translation function.
    
    Args:
        key: Translation key
        language: Optional language override
    
    Returns:
        Translated string
    """
    if language:
        return TRANSLATIONS.get(language, {}).get(key, key)
    return _i18n.t(key)

def set_language(language):
    """Set global language."""
    return _i18n.set_language(language)

def get_language():
    """Get current global language."""
    return _i18n.get_language()

def bilingual(key):
    """
    Get both English and French translations.
    
    Args:
        key: Translation key
    
    Returns:
        String in format "English / French"
    """
    en = TRANSLATIONS["en"].get(key, key)
    fr = TRANSLATIONS["fr"].get(key, key)
    return f"{en} / {fr}"
