"""
Network analysis module for visualizing connections between projects and users.
Analyzes collaboration patterns and community structures.
"""

from collections import defaultdict

class NetworkAnalyzer:
    """Analyzes project and user networks."""
    
    def __init__(self):
        self.projects = []
        self.connections = defaultdict(list)
    
    def add_projects(self, projects):
        """Add projects to the network."""
        self.projects.extend(projects)
        self._build_connections()
    
    def _build_connections(self):
        """Build connections between projects based on shared attributes."""
        for i, p1 in enumerate(self.projects):
            for p2 in self.projects[i+1:]:
                similarity = self._calculate_similarity(p1, p2)
                if similarity > 0:
                    self.connections[p1['full_name']].append({
                        'project': p2['full_name'],
                        'similarity': similarity
                    })
                    self.connections[p2['full_name']].append({
                        'project': p1['full_name'],
                        'similarity': similarity
                    })
    
    def _calculate_similarity(self, p1, p2):
        """Calculate similarity score between two projects."""
        score = 0
        
        # Language match
        if p1.get('language') == p2.get('language') and p1.get('language'):
            score += 3
        
        # Description overlap
        desc1 = set((p1.get('description') or '').lower().split())
        desc2 = set((p2.get('description') or '').lower().split())
        common_words = desc1 & desc2
        score += len(common_words) * 0.5
        
        # Similar size (stars)
        stars1 = p1.get('stargazers_count', 0)
        stars2 = p2.get('stargazers_count', 0)
        if stars1 > 0 and stars2 > 0:
            ratio = min(stars1, stars2) / max(stars1, stars2)
            score += ratio * 2
        
        return round(score, 2)
    
    def get_project_network(self, project_name, depth=1):
        """
        Get network of connected projects.
        
        Args:
            project_name: Name of the project
            depth: How many levels deep to search
        
        Returns:
            Dictionary of connections
        """
        network = {project_name: self.connections.get(project_name, [])}
        
        if depth > 1:
            for conn in network[project_name]:
                second_level = self.connections.get(conn['project'], [])
                network[conn['project']] = second_level
        
        return network
    
    def find_communities(self, min_connections=2):
        """
        Identify communities of related projects.
        
        Args:
            min_connections: Minimum connections to be in a community
        
        Returns:
            List of communities
        """
        communities = []
        visited = set()
        
        for project_name in self.connections:
            if project_name in visited:
                continue
            
            connections = self.connections[project_name]
            if len(connections) >= min_connections:
                community = [project_name]
                community.extend([c['project'] for c in connections])
                communities.append(list(set(community)))
                visited.update(community)
        
        return communities
    
    def get_central_projects(self, limit=10):
        """
        Get most central projects (with most connections).
        
        Returns:
            List of (project_name, connection_count) tuples
        """
        centrality = [
            (name, len(connections))
            for name, connections in self.connections.items()
        ]
        centrality.sort(key=lambda x: x[1], reverse=True)
        return centrality[:limit]
    
    def analyze_collaboration_potential(self, project1_name, project2_name):
        """
        Analyze potential for collaboration between two projects.
        
        Returns:
            Dictionary with analysis results
        """
        p1 = next((p for p in self.projects if p['full_name'] == project1_name), None)
        p2 = next((p for p in self.projects if p['full_name'] == project2_name), None)
        
        if not p1 or not p2:
            return {"potential": "unknown", "score": 0}
        
        similarity = self._calculate_similarity(p1, p2)
        
        reasons = []
        if p1.get('language') == p2.get('language'):
            reasons.append(f"Both use {p1.get('language')}")
        
        if similarity > 5:
            reasons.append("High technical similarity")
        
        if p1.get('stargazers_count', 0) > 500 and p2.get('stargazers_count', 0) > 500:
            reasons.append("Both have active communities")
        
        potential = "high" if similarity > 5 else "medium" if similarity > 2 else "low"
        
        return {
            "potential": potential,
            "score": similarity,
            "reasons": reasons
        }

def visualize_network_text(network):
    """
    Create a text-based visualization of the network.
    
    Args:
        network: Network dictionary
    
    Returns:
        String representation
    """
    output = ["\n🌐 PROJECT NETWORK VISUALIZATION\n"]
    output.append("=" * 60)
    
    for project, connections in network.items():
        output.append(f"\n📦 {project}")
        output.append(f"   Connected to {len(connections)} projects:")
        
        for conn in connections[:5]:  # Limit to top 5
            output.append(f"   ├─ {conn['project']} (similarity: {conn['similarity']})")
        
        if len(connections) > 5:
            output.append(f"   └─ ... and {len(connections) - 5} more")
    
    output.append("\n" + "=" * 60)
    return "\n".join(output)

def analyze_ecosystem(projects):
    """
    Analyze the entire ecosystem of projects.
    
    Args:
        projects: List of project dictionaries
    
    Returns:
        Ecosystem analysis dictionary
    """
    analyzer = NetworkAnalyzer()
    analyzer.add_projects(projects)
    
    return {
        "total_projects": len(projects),
        "total_connections": sum(len(c) for c in analyzer.connections.values()) // 2,
        "communities": len(analyzer.find_communities()),
        "central_projects": analyzer.get_central_projects(5),
        "network_density": _calculate_network_density(analyzer)
    }

def _calculate_network_density(analyzer):
    """Calculate network density (0-1)."""
    n = len(analyzer.projects)
    if n <= 1:
        return 0
    
    max_possible = n * (n - 1) / 2
    actual = sum(len(c) for c in analyzer.connections.values()) / 2
    
    return round(actual / max_possible, 3) if max_possible > 0 else 0

def suggest_collaborators(project_name, projects, limit=5):
    """
    Suggest potential collaborators for a project.
    
    Args:
        project_name: Name of the project
        projects: List of all projects
        limit: Number of suggestions
    
    Returns:
        List of suggested projects
    """
    analyzer = NetworkAnalyzer()
    analyzer.add_projects(projects)
    
    connections = analyzer.connections.get(project_name, [])
    connections.sort(key=lambda x: x['similarity'], reverse=True)
    
    suggestions = []
    for conn in connections[:limit]:
        project = next((p for p in projects if p['full_name'] == conn['project']), None)
        if project:
            suggestions.append({
                "project": conn['project'],
                "similarity": conn['similarity'],
                "url": project.get('html_url'),
                "stars": project.get('stargazers_count', 0)
            })
    
    return suggestions
