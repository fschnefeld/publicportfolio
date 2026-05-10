import streamlit as st

from data_handling.content import Project


def _project_row(project: Project) -> str:
    pills = "".join(f'<span class="pill">{p}</span>' for p in project["pills"])
    return (
        f'<div class="project-row">'
        f'<span class="project-num">{project["num"]}</span>'
        f"<div>"
        f'<div class="project-title">{project["title"]}</div>'
        f'<p class="project-body">{project["body"]}</p>'
        f"<div>{pills}</div>"
        f'<div class="project-impact">{project["impact"]}</div>'
        f"</div>"
        f'<span class="project-year">{project["year"]}</span>'
        f"</div>"
    )


def render_projects(projects: list[Project]) -> None:
    rows = "".join(_project_row(p) for p in projects)

    st.markdown(f"""
<section class="section" id="projects">
  <p class="section-label">03 — Selected Work</p>
  <h2 class="section-title">Projects that<br><em>shipped.</em></h2>
  <div class="projects-list">
    {rows}
  </div>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
