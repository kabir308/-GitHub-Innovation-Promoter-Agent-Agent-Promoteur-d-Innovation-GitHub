"""
Interactive web dashboard for GitHub Innovation Promoter.
Built with Streamlit for visualizing projects and analytics.
"""

import streamlit as st
import pandas as pd
from datetime import datetime

def show_dashboard(projects):
    """
    Display the main dashboard with projects and analytics.
    
    Args:
        projects: List of project dictionaries
    """
    st.set_page_config(
        page_title="GitHub Innovation Promoter",
        page_icon="🚀",
        layout="wide"
    )
    
    # Header
    st.title("🌟 GitHub Innovation Promoter / Agent Promoteur d'Innovation GitHub")
    st.markdown("---")
    
    # Sidebar for filters
    st.sidebar.header("🔍 Filters / Filtres")
    
    # Language filter
    languages = list(set([p.get("language", "Unknown") for p in projects if p.get("language")]))
    selected_languages = st.sidebar.multiselect(
        "Select Languages / Langues",
        languages,
        default=languages[:3] if len(languages) >= 3 else languages
    )
    
    # Stars filter
    min_stars = st.sidebar.slider(
        "Minimum Stars / Étoiles minimum",
        min_value=0,
        max_value=max([p.get("stargazers_count", 0) for p in projects]) if projects else 1000,
        value=0
    )
    
    # Filter projects
    filtered_projects = [
        p for p in projects
        if (not selected_languages or p.get("language") in selected_languages)
        and p.get("stargazers_count", 0) >= min_stars
    ]
    
    # Key metrics
    _show_metrics(filtered_projects)
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Projects / Projets",
        "📊 Analytics / Analytiques",
        "🎯 Recommendations",
        "📈 Trends / Tendances"
    ])
    
    with tab1:
        _show_projects_list(filtered_projects)
    
    with tab2:
        _show_analytics(filtered_projects)
    
    with tab3:
        _show_recommendations(filtered_projects)
    
    with tab4:
        _show_trends(filtered_projects)

def _show_metrics(projects):
    """Display key metrics in columns."""
    col1, col2, col3, col4 = st.columns(4)
    
    total_stars = sum(p.get("stargazers_count", 0) for p in projects)
    total_forks = sum(p.get("forks_count", 0) for p in projects)
    avg_score = sum(p.get("innovation_score", 0) for p in projects) / len(projects) if projects else 0
    
    with col1:
        st.metric("Total Projects", len(projects))
    with col2:
        st.metric("Total Stars ⭐", f"{total_stars:,}")
    with col3:
        st.metric("Total Forks 🍴", f"{total_forks:,}")
    with col4:
        st.metric("Avg Innovation Score", f"{avg_score:.1f}")
    
    st.markdown("---")

def _show_projects_list(projects):
    """Display list of projects."""
    st.subheader("Innovative Projects / Projets Innovants")
    
    if not projects:
        st.warning("No projects found / Aucun projet trouvé")
        return
    
    # Sort options
    sort_by = st.selectbox(
        "Sort by / Trier par",
        ["Stars", "Forks", "Innovation Score", "Name"]
    )
    
    # Sort projects
    if sort_by == "Stars":
        projects = sorted(projects, key=lambda x: x.get("stargazers_count", 0), reverse=True)
    elif sort_by == "Forks":
        projects = sorted(projects, key=lambda x: x.get("forks_count", 0), reverse=True)
    elif sort_by == "Innovation Score":
        projects = sorted(projects, key=lambda x: x.get("innovation_score", 0), reverse=True)
    else:
        projects = sorted(projects, key=lambda x: x.get("full_name", ""))
    
    # Display projects in cards
    for project in projects:
        with st.expander(f"🚀 {project['full_name']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Description:** {project.get('description', 'N/A')}")
                st.markdown(f"**Language:** {project.get('language', 'N/A')}")
                
                # Metrics in columns
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("⭐ Stars", project.get("stargazers_count", 0))
                m2.metric("🍴 Forks", project.get("forks_count", 0))
                m3.metric("👀 Watchers", project.get("watchers_count", 0))
                m4.metric("🎯 Score", project.get("innovation_score", 0))
            
            with col2:
                st.markdown(f"[View on GitHub]({project['html_url']})")
                # Display badge with error handling
                try:
                    st.image("badges/projet_innovant.svg", width=120)
                except Exception:
                    st.markdown("🏆 Innovation Badge")  # Fallback if image not found

def _show_analytics(projects):
    """Display analytics and visualizations."""
    st.subheader("📊 Analytics Dashboard")
    
    if not projects:
        st.warning("No data available")
        return
    
    # Create DataFrame
    df = pd.DataFrame([{
        "Name": p.get("full_name", ""),
        "Stars": p.get("stargazers_count", 0),
        "Forks": p.get("forks_count", 0),
        "Language": p.get("language", "Unknown"),
        "Innovation Score": p.get("innovation_score", 0)
    } for p in projects])
    
    # Language distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Language Distribution**")
        lang_counts = df["Language"].value_counts()
        st.bar_chart(lang_counts)
    
    with col2:
        st.write("**Top Projects by Stars**")
        top_projects = df.nlargest(5, "Stars")[["Name", "Stars"]]
        st.dataframe(top_projects, hide_index=True)
    
    # Statistics
    st.write("**Statistical Overview**")
    st.dataframe(df.describe(), use_container_width=True)

def _show_recommendations(projects):
    """Display personalized recommendations."""
    st.subheader("🎯 Personalized Recommendations")
    
    st.write("Based on your interests, we recommend exploring these projects:")
    
    # Simple recommendation: highest innovation score
    recommended = sorted(projects, key=lambda x: x.get("innovation_score", 0), reverse=True)[:5]
    
    for i, project in enumerate(recommended, 1):
        st.write(f"**{i}. {project['full_name']}**")
        st.write(f"   {project.get('description', 'No description')[:100]}...")
        st.write(f"   🎯 Innovation Score: {project.get('innovation_score', 0)} | ⭐ {project.get('stargazers_count', 0)} stars")
        st.write(f"   [Explore →]({project['html_url']})")
        st.write("")

def _show_trends(projects):
    """Display trending information."""
    st.subheader("📈 Trends & Insights")
    
    # Most popular languages
    languages = {}
    for p in projects:
        lang = p.get("language", "Unknown")
        languages[lang] = languages.get(lang, 0) + 1
    
    st.write("**Most Popular Languages**")
    for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]:
        st.write(f"- {lang}: {count} projects")
    
    st.write("")
    st.write("**Innovation Hotspots**")
    st.write("Projects with highest community engagement:")
    
    # Engagement = stars + forks + watchers
    engaged = sorted(
        projects,
        key=lambda x: x.get("stargazers_count", 0) + x.get("forks_count", 0) + x.get("watchers_count", 0),
        reverse=True
    )[:5]
    
    for p in engaged:
        engagement = p.get("stargazers_count", 0) + p.get("forks_count", 0) + p.get("watchers_count", 0)
        st.write(f"- **{p['full_name']}**: {engagement} total engagement")

def run_dashboard():
    """Run the dashboard application."""
    # This would be called with actual projects
    st.write("Dashboard is ready! Pass projects to show_dashboard() function.")
