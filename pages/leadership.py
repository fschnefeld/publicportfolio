import streamlit as st

from data_handling.content import Principle, TeamMember


def _principle_item(principle: Principle) -> str:
    return (
        f'<li class="principle-item">'
        f'<span class="principle-num">{principle["num"]}</span>'
        f"<div>"
        f'<div class="principle-title">{principle["title"]}</div>'
        f'<div class="principle-body">{principle["body"]}</div>'
        f"</div>"
        f"</li>"
    )


def _team_card(member: TeamMember) -> str:
    return (
        f'<div class="team-card">'
        f'<span class="team-role">{member["role"]}</span>'
        f'<span class="team-badge {member["badge_class"]}">{member["badge_label"]}</span>'
        f"</div>"
    )


def render_leadership(principles: list[Principle], team: list[TeamMember]) -> None:
    principle_items = "".join(_principle_item(p) for p in principles)
    team_cards = "".join(_team_card(m) for m in team)

    st.markdown(f"""
<section class="section-alt" id="leadership">
  <p class="section-label">04 — Leadership</p>
  <h2 class="section-title">How I lead<br><em>teams.</em></h2>

  <div class="leadership-grid">
    <div>
      <p class="section-body">
        I've grown from individual contributor to a lead responsible for a multi-disciplinary team
        spanning data science, engineering, analytics, and ML infrastructure.
        My approach is rooted in clarity, psychological safety, and holding a high bar — technically and professionally.
      </p>
      <ul class="principle-list">
        {principle_items}
      </ul>
    </div>
    <div>
      <p class="section-label" style="margin-bottom:1.5rem;">Current Team Structure</p>
      <div class="team-card-wrap">
        {team_cards}
      </div>
    </div>
  </div>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
