import streamlit as st


def render_philosophy() -> None:
    st.markdown("""
<section class="philosophy-strip">
  <p class="philosophy-quote">
    "The job of a data leader isn't to have all the answers —
    it's to build a team that asks better questions."
  </p>
  <p class="philosophy-attr">Management Philosophy</p>
</section>
""", unsafe_allow_html=True)
