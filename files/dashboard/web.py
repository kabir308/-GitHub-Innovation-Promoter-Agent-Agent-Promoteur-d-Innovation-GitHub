# Example Streamlit skeleton / Exemple de squelette Streamlit
import streamlit as st

def show_dashboard(projects):
    st.title("GitHub Innovative Projects / Projets Innovants GitHub")
    for project in projects:
        st.subheader(project['full_name'])
        st.write(project['description'])
        st.write(f"⭐ Stars: {project['stargazers_count']}")
        st.write(f"[Repo link / Lien vers le repo]({project['html_url']})")