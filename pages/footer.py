import streamlit as st


def render_footer() -> None:
    st.markdown("""
<footer class="footer">
  <span class="footer-left">◈ ANALYTICS & DATA SCIENCE LEAD — PORTFOLIO 2026</span>
  <span class="footer-right">BUILT WITH STREAMLIT</span>
</footer>
""", unsafe_allow_html=True)
