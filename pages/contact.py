import streamlit as st


def render_contact() -> None:
    st.markdown("""
<section class="section" id="contact">
  <p class="section-label">05 — Contact</p>
  <h2 class="section-title">Let's talk about<br><em>what's next.</em></h2>

  <div class="contact-grid">
    <div>
      <p class="section-body">
        I'm selectively exploring Head of Data, Director of Analytics, and VP of Data roles
        — ideally in a product-led company where data is a genuine strategic asset, not an afterthought.
      </p>
      <p class="section-body" style="margin-top:1rem;">
        I'm especially interested in orgs that are scaling their data platform,
        navigating a BI → ML maturity shift, or building out a first-class analytics function.
      </p>
      <div class="available-badge">
        <span class="available-dot"></span>
        OPEN TO CONVERSATIONS
      </div>
    </div>

    <div class="contact-links">
      <a class="contact-link" href="mailto:your.email@example.com">
        <span class="contact-icon">✉</span>
        <span class="contact-label">your.email@example.com</span>
        <span class="contact-meta">EMAIL</span>
      </a>
      <a class="contact-link" href="https://linkedin.com/in/yourprofile" target="_blank">
        <span class="contact-icon">in</span>
        <span class="contact-label">linkedin.com/in/yourprofile</span>
        <span class="contact-meta">LINKEDIN</span>
      </a>
      <a class="contact-link" href="https://github.com/yourgithub" target="_blank">
        <span class="contact-icon">⌥</span>
        <span class="contact-label">github.com/yourgithub</span>
        <span class="contact-meta">GITHUB</span>
      </a>
    </div>

  </div>
</section>
<div class="divider"></div>
""", unsafe_allow_html=True)
