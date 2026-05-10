import streamlit as st

from data_handling.content import Stat


def render_about(stats: list[Stat]) -> None:
    stat_cards = "".join(
        f'<div class="stat-card">'
        f'<div class="stat-num">{s["num"]}</div>'
        f'<div class="stat-label">{s["label"]}</div>'
        f"</div>"
        for s in stats
    )

    st.markdown(f"""
<section class="section" id="about">
  <p class="section-label">01 — About</p>
  <h2 class="section-title">Technical depth.<br><em>Strategic breadth.</em></h2>
  <div class="about-grid">
    <div>
      <p class="section-body">
        I'm a data and analytics lead with a background in building production-grade forecasting systems,
        data platforms, and cross-functional analytics teams — primarily in the retail and e-commerce space.
      </p>
      <p class="section-body" style="margin-top:1.25rem;">
        Over the years I've moved from writing the SQL and dbt models myself to owning the entire
        data stack: infrastructure decisions, team structure, stakeholder alignment, and the roadmap that
        ties it all together. My goal is to bring that full-stack perspective into a formal leadership role.
      </p>
      <p class="section-body" style="margin-top:1.25rem;">
        I believe great data leaders don't stop being curious about the craft — they use it to ask better
        questions, spot architectural risks early, and earn the trust of the people they manage.
      </p>
      <div class="available-badge" style="margin-top:2rem;">
        <span class="available-dot"></span>
        OPEN TO MANAGEMENT OPPORTUNITIES
      </div>
    </div>
    <div class="about-stat-grid">
      {stat_cards}
    </div>
  </div>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
