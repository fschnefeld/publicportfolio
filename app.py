import streamlit as st

from data_handling.content import PRINCIPLES, PROJECTS, SKILLS, STATS, TEAM
from pages import about, contact, expertise, footer, hero, leadership, nav, philosophy, projects
from theme.theme import inject_css

st.set_page_config(
    page_title="Portfolio · Analytics & Data Science Lead",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
nav.render_nav()
hero.render_hero()
about.render_about(STATS)
expertise.render_expertise(SKILLS)
projects.render_projects(PROJECTS)
philosophy.render_philosophy()
leadership.render_leadership(PRINCIPLES, TEAM)
contact.render_contact()
footer.render_footer()
