import modules.detect as detect
import modules.promote as promote

def main():
    print("🌟 Agent Promoteur d'Innovation GitHub démarre / Innovation Promoter Agent starting...")
    projects = detect.get_innovative_projects()
    for project in projects:
        promote.promote_project(project)

if __name__ == "__main__":
    main()