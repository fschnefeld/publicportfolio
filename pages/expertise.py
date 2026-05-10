import streamlit as st

from data_handling.content import Skill


def _skill_card(skill: Skill) -> str:
    tags = "".join(f'<span class="stag">{t}</span>' for t in skill["tags"])
    return (
        f'<div class="skill-card">'
        f'<div class="skill-card-icon">{skill["icon"]}</div>'
        f'<div class="skill-card-title">{skill["title"]}</div>'
        f'<div class="skill-card-body">{skill["body"]}</div>'
        f'<div class="skill-tags">{tags}</div>'
        f"</div>"
    )


def render_expertise(skills: list[Skill]) -> None:
    cards = "".join(_skill_card(s) for s in skills)

    st.markdown(f"""
<section class="section-alt" id="expertise">
  <p class="section-label">02 — Expertise</p>
  <h2 class="section-title">What I bring<br>to the <em>table.</em></h2>
  <div class="skills-grid">
    {cards}
  </div>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
