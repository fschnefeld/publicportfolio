import streamlit as st


def render_nav() -> None:
    st.markdown("""
<nav class="nav">
  <span class="nav-logo">◈ Portfolio</span>
  <ul class="nav-links">
    <li><a href="#about" data-section="about">About</a></li>
    <li><a href="#expertise" data-section="expertise">Expertise</a></li>
    <li><a href="#projects" data-section="projects">Projects</a></li>
    <li><a href="#leadership" data-section="leadership">Leadership</a></li>
    <li><a href="#contact" data-section="contact">Contact</a></li>
  </ul>
</nav>
""", unsafe_allow_html=True)
