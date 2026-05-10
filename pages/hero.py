import streamlit as st


def render_hero() -> None:
    st.markdown("""
<section class="hero" id="home">
  <p class="hero-eyebrow">Analytics & Data Science Lead → Management</p>
  <h1 class="hero-title">Turning data<br>into <em>direction.</em></h1>
  <p class="hero-sub">
    I build and lead high-performing data teams that translate complex analytical systems into strategic business outcomes.
    Currently exploring my next step into a Head of Data / Director of Analytics role.
  </p>
  <div class="hero-pills">
    <span class="pill">Demand Forecasting</span>
    <span class="pill">Data Platform Architecture</span>
    <span class="pill">Team Leadership</span>
    <span class="pill">dbt · Dagster · MLflow</span>
    <span class="pill">Prophet · EM · LightGBM</span>
    <span class="pill">SQL · Python</span>
  </div>
  <a class="hero-cta" href="#contact">Open to opportunities</a>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
