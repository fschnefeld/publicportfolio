import streamlit as st


def render_nav() -> None:
    st.markdown("""
<nav class="nav">
  <span class="nav-logo">◈ Portfolio</span>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#expertise">Expertise</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#leadership">Leadership</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
""", unsafe_allow_html=True)
