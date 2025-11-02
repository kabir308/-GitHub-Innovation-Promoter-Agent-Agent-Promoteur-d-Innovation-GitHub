# 📚 GitHub Innovation Promoter - Complete Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Configuration](#configuration)
6. [Modules](#modules)
7. [Usage Examples](#usage-examples)
8. [API Reference](#api-reference)
9. [Contributing](#contributing)

## Introduction

The GitHub Innovation Promoter Agent is a comprehensive, open-source system designed to discover, analyze, promote, and facilitate collaboration around innovative projects on GitHub.

### Key Capabilities
- 🔍 **Smart Detection**: Automatically discover innovative projects using AI and multiple criteria
- 🤖 **AI Analysis**: Advanced sentiment analysis, technology detection, and trend prediction
- 🎯 **Recommendations**: Personalized project recommendations based on user interests
- 📊 **Analytics**: Interactive dashboard with visualizations and insights
- 🌐 **Network Analysis**: Identify communities and collaboration opportunities
- 📱 **Social Media**: Ready-to-post content for Twitter and LinkedIn
- 🔔 **Notifications**: Customizable notification system
- 🌍 **Multilingual**: Full support for English and French
- 📈 **Feedback System**: Collect and analyze community feedback

## Features

### 1. Project Detection (`modules/detect.py`)
- Searches GitHub repositories using multiple keywords
- Applies customizable criteria (stars, forks, activity)
- Calculates innovation scores
- Handles API rate limiting gracefully

### 2. Project Promotion (`modules/promote.py`)
- Multiple output formats: console, JSON, Markdown, HTML
- Comprehensive project information display
- Badge generation for innovative projects

### 3. AI Analysis (`ai/advanced_analysis.py`)
- Technology stack detection
- Sentiment analysis of descriptions
- Trending score calculation
- Project maturity assessment
- Automated recommendations

### 4. Recommendation Engine (`modules/recommend.py`)
- Collaboration suggestions
- Similar project discovery
- Opportunity identification
- Interest-based filtering

### 5. Feedback Collection (`modules/feedback.py`)
- Rating system (1-5 stars)
- Comment collection
- Statistical analysis
- Top-rated project tracking

### 6. Network Analysis (`modules/network_analysis.py`)
- Project similarity detection
- Community identification
- Centrality analysis
- Collaboration potential assessment

### 7. Notification System (`modules/notifications.py`)
- Multiple channels: console, email, webhook
- Customizable preferences
- Notification history
- Batch notifications

### 8. Social Media Connectors
- **Twitter** (`connectors/twitter.py`): Tweet generation, thread creation
- **LinkedIn** (`connectors/linkedin.py`): Professional post formatting

### 9. Interactive Dashboard (`dashboard/web.py`)
- Real-time project visualization
- Filtering and sorting
- Analytics charts
- Trend analysis

### 10. Multilingual Support (`modules/i18n.py`)
- English and French translations
- Easy language switching
- Bilingual output options

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

```bash
# Clone the repository
git clone https://github.com/kabir308/-GitHub-Innovation-Promoter-Agent-Agent-Promoteur-d-Innovation-GitHub.git
cd -GitHub-Innovation-Promoter-Agent-Agent-Promoteur-d-Innovation-GitHub

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Run the Main Agent

```bash
python agent_promoteur.py
```

This will:
1. Detect innovative projects on GitHub
2. Analyze each project with AI
3. Generate recommendations
4. Perform network analysis
5. Create social media posts

### Run Interactive Mode

```bash
python agent_promoteur.py --interactive
```

### Launch Dashboard

```bash
streamlit run dashboard_app.py
```

### Run Examples

```bash
python examples.py
```

## Configuration

The agent uses `config.json` for configuration. Key settings:

```json
{
  "detection": {
    "keywords": ["ai", "machine learning", "blockchain"],
    "criteria": {
      "min_stars": 10,
      "min_forks": 5,
      "has_description": true
    },
    "limit": 20
  },
  "language": "en",
  "promotion": {
    "default_format": "console",
    "enabled_platforms": ["twitter", "linkedin"]
  },
  "notifications": {
    "channels": {
      "console": true,
      "email": false
    }
  }
}
```

### Configuration Options

- **detection.keywords**: List of keywords to search for
- **detection.criteria.min_stars**: Minimum stars required
- **detection.criteria.min_forks**: Minimum forks required
- **detection.limit**: Maximum projects to fetch
- **language**: UI language ("en" or "fr")
- **promotion.default_format**: Output format (console, json, markdown, html)
- **promotion.enabled_platforms**: Social media platforms to use

## Modules

### Detection Module
```python
from modules import detect

# Basic usage
projects = detect.get_innovative_projects(limit=10)

# With custom criteria
criteria = {
    "min_stars": 100,
    "min_forks": 20,
    "has_description": True
}
projects = detect.get_innovative_projects(limit=5, criteria=criteria)
```

### Promotion Module
```python
from modules import promote

# Console output
promote.promote_project(project, format="console")

# JSON output
json_data = promote.promote_project(project, format="json")

# Markdown output
markdown = promote.promote_project(project, format="markdown")
```

### AI Analysis Module
```python
from ai import advanced_analysis

analysis = advanced_analysis.analyze_project_with_ai(project)
# Returns: is_innovative, technologies, sentiment, trending_score, maturity_level, recommendation
```

### Recommendation Module
```python
from modules import recommend

# Get recommendations
recommendations = recommend.recommend_collaborations(
    projects, 
    user_interests=["ai", "python"],
    limit=5
)

# Find similar projects
similar = recommend.find_similar_projects(target_project, all_projects, limit=5)

# Get opportunities
opportunities = recommend.suggest_opportunities(project)
```

### Feedback Module
```python
from modules.feedback import FeedbackCollector

collector = FeedbackCollector()
collector.add_feedback("owner/repo", rating=5, comment="Great project!")
stats = collector.get_project_stats("owner/repo")
```

### Network Analysis Module
```python
from modules.network_analysis import NetworkAnalyzer

analyzer = NetworkAnalyzer()
analyzer.add_projects(projects)
communities = analyzer.find_communities()
central = analyzer.get_central_projects(limit=10)
```

### Notification Module
```python
from modules.notifications import NotificationManager

notifier = NotificationManager()
notifier.send_notification("new_project", project, "Custom message")
notifier.check_and_notify(project)  # Send if matches preferences
```

## Usage Examples

### Example 1: Basic Project Discovery

```python
from modules import detect, promote

projects = detect.get_innovative_projects(limit=5)
for project in projects:
    promote.promote_project(project)
```

### Example 2: AI-Powered Analysis

```python
from modules import detect
from ai import advanced_analysis

projects = detect.get_innovative_projects(limit=1)
if projects:
    analysis = advanced_analysis.analyze_project_with_ai(projects[0])
    print(f"Innovation Score: {analysis['trending_score']}")
    print(f"Technologies: {analysis['technologies']}")
```

### Example 3: Get Recommendations

```python
from modules import detect, recommend

projects = detect.get_innovative_projects(limit=20)
recommendations = recommend.recommend_collaborations(
    projects,
    user_interests=["machine learning", "python"],
    limit=5
)

for rec in recommendations:
    print(f"{rec['project']['full_name']} - Score: {rec['relevance_score']}")
```

### Example 4: Social Media Promotion

```python
from modules import detect
from connectors import twitter, linkedin

projects = detect.get_innovative_projects(limit=1)
if projects:
    twitter.publish_to_twitter(projects[0])
    linkedin.publish_to_linkedin(projects[0])
```

### Example 5: Network Analysis

```python
from modules import detect, network_analysis

projects = detect.get_innovative_projects(limit=20)
ecosystem = network_analysis.analyze_ecosystem(projects)

print(f"Total Connections: {ecosystem['total_connections']}")
print(f"Communities: {ecosystem['communities']}")
```

## API Reference

### Detection API
- `get_innovative_projects(limit=10, criteria=None)` - Get innovative projects
- `_meets_criteria(project, criteria)` - Check if project meets criteria
- `_calculate_innovation_score(project)` - Calculate innovation score

### Promotion API
- `promote_project(project, format="console")` - Promote a project
- Formats: "console", "json", "markdown", "html"

### AI Analysis API
- `analyze_project_with_ai(project)` - Comprehensive AI analysis
- `detect_technologies(project)` - Detect technology stack
- `analyze_sentiment(text)` - Sentiment analysis
- `calculate_trending_score(project)` - Calculate trending score
- `assess_maturity(project)` - Assess project maturity

### Recommendation API
- `recommend_collaborations(projects, user_interests, limit)` - Get recommendations
- `find_similar_projects(target, all_projects, limit)` - Find similar projects
- `suggest_opportunities(project)` - Suggest contribution opportunities

### Network Analysis API
- `NetworkAnalyzer.add_projects(projects)` - Add projects to network
- `NetworkAnalyzer.find_communities()` - Identify communities
- `NetworkAnalyzer.get_central_projects(limit)` - Get most central projects
- `analyze_ecosystem(projects)` - Full ecosystem analysis

## Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- New detection criteria
- Additional social media connectors
- Enhanced AI/ML models
- Dashboard improvements
- New visualization types
- Additional languages for i18n
- Performance optimizations
- Documentation improvements

## License

MIT License - See LICENSE file for details

## Support

- Open an issue for bug reports
- Submit feature requests via issues
- Check the examples.py file for usage patterns
- Review the Feature Proposals.md for upcoming features

---

**Made with ❤️ for the open-source community**
