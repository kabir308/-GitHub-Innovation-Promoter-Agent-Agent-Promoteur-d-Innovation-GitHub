# 🚀 Getting Started Guide

## Welcome to GitHub Innovation Promoter!

This guide will help you get started quickly with the GitHub Innovation Promoter Agent.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for accessing GitHub API)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/kabir308/-GitHub-Innovation-Promoter-Agent-Agent-Promoteur-d-Innovation-GitHub.git
cd -GitHub-Innovation-Promoter-Agent-Agent-Promoteur-d-Innovation-GitHub
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `requests` - For GitHub API calls
- `streamlit` - For the interactive dashboard
- `pandas` - For data manipulation
- `matplotlib` - For visualizations
- `plotly` - For interactive charts

## Quick Start Options

### Option 1: Run the Main Agent

The simplest way to start:

```bash
python agent_promoteur.py
```

This will:
1. Detect innovative projects from GitHub
2. Analyze them with AI
3. Generate recommendations
4. Perform network analysis
5. Create social media posts

**Output**: Console-based report with all insights

### Option 2: Interactive Mode

For a menu-driven experience:

```bash
python agent_promoteur.py --interactive
```

You'll see a menu with options:
1. Detect and promote projects
2. Analyze specific project
3. Get recommendations
4. View network analysis
5. Launch dashboard
6. Exit

### Option 3: Interactive Dashboard

For a visual, web-based interface:

```bash
streamlit run dashboard_app.py
```

This opens a web browser with:
- Project listings with filters
- Analytics and charts
- Recommendations
- Trend analysis

**Access**: Opens automatically at http://localhost:8501

### Option 4: Run Examples

To see all features in action:

```bash
python examples.py
```

Choose from 9 different examples showing various features.

## Configuration

### Basic Configuration

Edit `config.json` to customize behavior:

```json
{
  "detection": {
    "keywords": ["ai", "machine learning", "blockchain"],
    "criteria": {
      "min_stars": 10,
      "min_forks": 5
    },
    "limit": 20
  },
  "language": "en",
  "promotion": {
    "enabled_platforms": ["twitter", "linkedin"]
  }
}
```

### Configuration Options Explained

**detection.keywords**: What to search for on GitHub
- Add/remove keywords based on your interests
- Examples: "ai", "web3", "devops", "mobile"

**detection.criteria.min_stars**: Minimum GitHub stars
- Higher = more established projects
- Lower = discover newer projects

**detection.limit**: How many projects to fetch
- 10-20 is good for quick analysis
- 50+ for comprehensive reports

**language**: UI language
- "en" for English
- "fr" for French

**promotion.enabled_platforms**: Which social media to use
- "twitter" for Twitter/X posts
- "linkedin" for LinkedIn posts

## Common Use Cases

### Use Case 1: Daily Innovation Discovery

Run this daily to discover new projects:

```bash
python agent_promoteur.py
```

**What you get**: List of innovative projects with analysis

### Use Case 2: Find Projects to Contribute To

```python
from modules import detect, recommend

projects = detect.get_innovative_projects(limit=20)
for project in projects:
    opportunities = recommend.suggest_opportunities(project)
    if opportunities:
        print(f"{project['full_name']}: {len(opportunities)} opportunities")
```

**What you get**: Projects with contribution opportunities

### Use Case 3: Share on Social Media

```python
from modules import detect
from connectors import twitter, linkedin

projects = detect.get_innovative_projects(limit=1)
twitter.publish_to_twitter(projects[0])
linkedin.publish_to_linkedin(projects[0])
```

**What you get**: Ready-to-post social media content

### Use Case 4: Analyze a Specific Project

```python
from modules import detect
from ai import advanced_analysis

# Search for a specific project
projects = detect.get_innovative_projects(limit=50)
target = [p for p in projects if "tensorflow" in p['full_name'].lower()][0]

# Analyze it
analysis = advanced_analysis.analyze_project_with_ai(target)
print(analysis)
```

**What you get**: Detailed AI analysis of the project

### Use Case 5: Network Analysis

```python
from modules import detect, network_analysis

projects = detect.get_innovative_projects(limit=30)
ecosystem = network_analysis.analyze_ecosystem(projects)

print(f"Communities: {ecosystem['communities']}")
print(f"Network density: {ecosystem['network_density']}")
```

**What you get**: Understanding of project relationships

## Troubleshooting

### Issue: Rate Limiting

**Problem**: "Rate limit reached" message

**Solution**: 
- The system automatically uses demo data as fallback
- Wait 60 minutes for rate limit to reset
- Add GitHub API token to config.json (optional)

### Issue: Module Import Errors

**Problem**: "ModuleNotFoundError"

**Solution**:
```bash
pip install -r requirements.txt
```

### Issue: Dashboard Won't Start

**Problem**: Streamlit errors

**Solution**:
```bash
pip install --upgrade streamlit
streamlit run dashboard_app.py
```

### Issue: No Projects Found

**Problem**: Empty results

**Solution**:
- Check internet connection
- Verify GitHub is accessible
- Try different keywords in config.json
- Lower min_stars criteria

## Next Steps

### Learn More

1. Read [DOCUMENTATION.md](DOCUMENTATION.md) for complete API reference
2. Check [examples.py](examples.py) for code samples
3. Review [Feature Proposals.md](Feature%20Proposals.md) for upcoming features

### Customize

1. Edit `config.json` for your interests
2. Modify detection criteria
3. Add your own keywords
4. Adjust notification preferences

### Contribute

1. Fork the repository
2. Add new features
3. Submit pull requests
4. Report issues

## Tips for Success

### Best Practices

1. **Start Small**: Begin with limit=10, increase gradually
2. **Customize Keywords**: Use keywords relevant to your domain
3. **Check Daily**: Run once per day to discover new projects
4. **Use Dashboard**: Visual analysis is more insightful
5. **Share Findings**: Use social media connectors to share discoveries

### Advanced Usage

For power users:

```python
# Combine multiple features
from modules import detect, recommend, network_analysis
from ai import advanced_analysis

# 1. Detect projects
projects = detect.get_innovative_projects(limit=50)

# 2. Filter by AI analysis
innovative = [p for p in projects 
              if advanced_analysis.analyze_project_with_ai(p)['is_innovative']]

# 3. Get recommendations
recs = recommend.recommend_collaborations(innovative, 
                                         user_interests=["ai", "python"])

# 4. Analyze network
ecosystem = network_analysis.analyze_ecosystem(innovative)

# 5. Get collaboration suggestions
for project in innovative[:5]:
    similar = recommend.find_similar_projects(project, innovative)
    print(f"{project['full_name']}: {len(similar)} similar projects")
```

## Support

- 🐛 **Issues**: Report bugs via GitHub Issues
- 💡 **Features**: Suggest features via GitHub Issues
- 📚 **Documentation**: Check DOCUMENTATION.md
- 💬 **Questions**: Open a discussion on GitHub

## License

MIT License - Free to use, modify, and distribute

---

**Happy Innovation Hunting! 🚀**

*Made with ❤️ for the open-source community*
