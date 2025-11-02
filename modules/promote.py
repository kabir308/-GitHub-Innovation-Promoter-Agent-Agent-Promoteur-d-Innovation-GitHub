import json

def promote_project(project, format="console"):
    """
    Promote a project in various formats.
    
    Args:
        project: Project dictionary
        format: Output format (console, json, markdown, html)
    """
    if format == "console":
        _promote_console(project)
    elif format == "json":
        return _promote_json(project)
    elif format == "markdown":
        return _promote_markdown(project)
    elif format == "html":
        return _promote_html(project)
    else:
        _promote_console(project)

def _promote_console(project):
    """Console/terminal output format."""
    print(f"\n{'='*60}")
    print(f"🚀 Innovative Project / Projet Innovant")
    print(f"{'='*60}")
    print(f"📦 Name: {project['full_name']}")
    print(f"📝 Description: {project.get('description', 'N/A')}")
    print(f"⭐ Stars: {project.get('stargazers_count', 0)}")
    print(f"🍴 Forks: {project.get('forks_count', 0)}")
    print(f"👀 Watchers: {project.get('watchers_count', 0)}")
    print(f"🐛 Open Issues: {project.get('open_issues_count', 0)}")
    print(f"💻 Language: {project.get('language', 'N/A')}")
    print(f"🎯 Innovation Score: {project.get('innovation_score', 'N/A')}")
    print(f"🔗 Link / Lien: {project['html_url']}")
    print(f"🏆 Badge: badges/projet_innovant.svg")
    print(f"{'='*60}\n")

def _promote_json(project):
    """JSON output format."""
    return json.dumps({
        "name": project['full_name'],
        "description": project.get('description'),
        "stars": project.get('stargazers_count', 0),
        "forks": project.get('forks_count', 0),
        "watchers": project.get('watchers_count', 0),
        "issues": project.get('open_issues_count', 0),
        "language": project.get('language'),
        "innovation_score": project.get('innovation_score'),
        "url": project['html_url'],
        "badge": "badges/projet_innovant.svg"
    }, indent=2)

def _promote_markdown(project):
    """Markdown output format."""
    return f"""## 🚀 {project['full_name']}

**Description:** {project.get('description', 'N/A')}

- ⭐ Stars: {project.get('stargazers_count', 0)}
- 🍴 Forks: {project.get('forks_count', 0)}
- 💻 Language: {project.get('language', 'N/A')}
- 🎯 Innovation Score: {project.get('innovation_score', 'N/A')}

[View on GitHub]({project['html_url']})

![Innovation Badge](badges/projet_innovant.svg)
"""

def _promote_html(project):
    """HTML output format."""
    return f"""<div class="innovative-project">
    <h2>🚀 {project['full_name']}</h2>
    <p><strong>Description:</strong> {project.get('description', 'N/A')}</p>
    <ul>
        <li>⭐ Stars: {project.get('stargazers_count', 0)}</li>
        <li>🍴 Forks: {project.get('forks_count', 0)}</li>
        <li>💻 Language: {project.get('language', 'N/A')}</li>
        <li>🎯 Innovation Score: {project.get('innovation_score', 'N/A')}</li>
    </ul>
    <a href="{project['html_url']}" target="_blank">View on GitHub</a>
    <br>
    <img src="badges/projet_innovant.svg" alt="Innovation Badge">
</div>"""