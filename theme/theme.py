import streamlit as st

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stApp"] {
    background: #0C0D11 !important;
    color: #E8E6DF !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stSidebarNav"] { display: none !important; }

/* ── Main container ── */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Section wrapper ── */
.section {
    padding: 5rem 8vw;
}
.section-alt {
    padding: 5rem 8vw;
    background: #111318;
}

/* ── Nav ── */
.nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 999;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 8vw;
    background: rgba(12, 13, 17, 0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.nav-logo {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.18em;
    color: #7B9E87;
    text-transform: uppercase;
}
.nav-links {
    display: flex;
    gap: 2.5rem;
    list-style: none;
    margin: 0; padding: 0;
}
.nav-links a {
    font-size: 0.82rem;
    letter-spacing: 0.06em;
    color: rgba(232,230,223,0.55);
    text-decoration: none;
    text-transform: uppercase;
    transition: color 0.2s;
}
.nav-links a:hover { color: #E8E6DF; }

/* ── Hero ── */
.hero {
    padding: 12rem 8vw 8rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -20%;
    right: -10%;
    width: 60vw;
    height: 60vw;
    background: radial-gradient(ellipse, rgba(123,158,135,0.08) 0%, transparent 65%);
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.22em;
    color: #7B9E87;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(3rem, 6vw, 6rem);
    line-height: 1.05;
    color: #E8E6DF;
    margin-bottom: 1.5rem;
    max-width: 14ch;
}
.hero-title em {
    font-style: italic;
    color: #7B9E87;
}
.hero-sub {
    font-size: 1.1rem;
    line-height: 1.7;
    color: rgba(232,230,223,0.6);
    max-width: 52ch;
    margin-bottom: 3rem;
    font-weight: 300;
}
.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 3.5rem;
}
.pill {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    padding: 0.35rem 0.8rem;
    border: 1px solid rgba(123,158,135,0.35);
    border-radius: 2px;
    color: #7B9E87;
    background: rgba(123,158,135,0.06);
}
.hero-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 0.85rem;
    letter-spacing: 0.08em;
    color: #0C0D11;
    background: #7B9E87;
    padding: 0.85rem 1.8rem;
    border-radius: 2px;
    text-decoration: none;
    font-weight: 500;
    transition: background 0.2s;
}
.hero-cta:hover { background: #90B49B; }

/* ── Section titles ── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.22em;
    color: #7B9E87;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 3.5vw, 3rem);
    line-height: 1.15;
    color: #E8E6DF;
    margin-bottom: 1rem;
}
.section-title em { font-style: italic; color: #7B9E87; }
.section-body {
    font-size: 1rem;
    line-height: 1.75;
    color: rgba(232,230,223,0.6);
    max-width: 60ch;
    font-weight: 300;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: rgba(255,255,255,0.06);
    margin: 0;
}

/* ── About grid ── */
.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5rem;
    margin-top: 4rem;
    align-items: start;
}
.about-stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-top: 2rem;
}
.stat-card {
    padding: 1.5rem;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 4px;
    background: rgba(255,255,255,0.02);
}
.stat-num {
    font-family: 'DM Serif Display', serif;
    font-size: 2.8rem;
    color: #7B9E87;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.stat-label {
    font-size: 0.82rem;
    color: rgba(232,230,223,0.5);
    line-height: 1.4;
}

/* ── Skills ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 3.5rem;
}
.skill-card {
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 4px;
    background: rgba(255,255,255,0.02);
    transition: border-color 0.25s, background 0.25s;
}
.skill-card:hover {
    border-color: rgba(123,158,135,0.3);
    background: rgba(123,158,135,0.04);
}
.skill-card-icon {
    font-size: 1.4rem;
    margin-bottom: 1rem;
}
.skill-card-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    color: #7B9E87;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.skill-card-body {
    font-size: 0.9rem;
    line-height: 1.65;
    color: rgba(232,230,223,0.55);
}
.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 1rem;
}
.stag {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    padding: 0.2rem 0.5rem;
    border-radius: 2px;
    background: rgba(123,158,135,0.1);
    color: #7B9E87;
    letter-spacing: 0.04em;
}

/* ── Projects ── */
.projects-list {
    margin-top: 4rem;
    display: flex;
    flex-direction: column;
    gap: 0;
}
.project-row {
    display: grid;
    grid-template-columns: 3rem 1fr auto;
    align-items: start;
    gap: 2rem;
    padding: 2.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    transition: background 0.2s;
}
.project-row:first-child { border-top: 1px solid rgba(255,255,255,0.06); }
.project-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: rgba(123,158,135,0.5);
    padding-top: 0.25rem;
}
.project-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    color: #E8E6DF;
    margin-bottom: 0.5rem;
}
.project-body {
    font-size: 0.9rem;
    line-height: 1.7;
    color: rgba(232,230,223,0.55);
    max-width: 65ch;
    margin-bottom: 0.75rem;
}
.project-impact {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #7B9E87;
    padding: 0.3rem 0.6rem;
    border: 1px solid rgba(123,158,135,0.25);
    border-radius: 2px;
    display: inline-block;
    margin-top: 0.5rem;
}
.project-year {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: rgba(232,230,223,0.3);
    padding-top: 0.25rem;
    white-space: nowrap;
}

/* ── Leadership ── */
.leadership-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    margin-top: 4rem;
    align-items: start;
}
.principle-list {
    list-style: none;
    padding: 0;
    margin: 2rem 0 0;
}
.principle-item {
    display: flex;
    gap: 1.2rem;
    padding: 1.25rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.principle-item:last-child { border-bottom: none; }
.principle-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #7B9E87;
    padding-top: 0.25rem;
    flex-shrink: 0;
}
.principle-title {
    font-size: 0.95rem;
    font-weight: 500;
    color: #E8E6DF;
    margin-bottom: 0.3rem;
}
.principle-body {
    font-size: 0.87rem;
    line-height: 1.65;
    color: rgba(232,230,223,0.5);
}
.team-card-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}
.team-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.25rem;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 4px;
    background: rgba(255,255,255,0.02);
}
.team-role {
    font-size: 0.88rem;
    color: rgba(232,230,223,0.75);
}
.team-badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    padding: 0.2rem 0.55rem;
    border-radius: 2px;
    letter-spacing: 0.05em;
}
.badge-ds { background: rgba(123,158,135,0.15); color: #7B9E87; }
.badge-eng { background: rgba(99,125,169,0.15); color: #8EB0D6; }
.badge-analytics { background: rgba(169,140,99,0.15); color: #D6B98E; }

/* ── Philosophy strip ── */
.philosophy-strip {
    padding: 6rem 8vw;
    background: #7B9E87;
    text-align: center;
}
.philosophy-quote {
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    color: #0C0D11;
    max-width: 42ch;
    margin: 0 auto 1.5rem;
    line-height: 1.3;
}
.philosophy-attr {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    color: rgba(12,13,17,0.55);
    text-transform: uppercase;
}

/* ── Contact ── */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
    align-items: center;
    margin-top: 4rem;
}
.contact-links {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 2rem;
}
.contact-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.2rem 1.5rem;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 4px;
    text-decoration: none;
    color: #E8E6DF;
    font-size: 0.9rem;
    transition: border-color 0.2s, background 0.2s;
    background: rgba(255,255,255,0.02);
}
.contact-link:hover {
    border-color: rgba(123,158,135,0.4);
    background: rgba(123,158,135,0.05);
}
.contact-icon {
    font-size: 1rem;
    width: 1.5rem;
    text-align: center;
}
.contact-label {
    flex: 1;
}
.contact-meta {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: rgba(232,230,223,0.35);
}
.available-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    color: #7B9E87;
    padding: 0.4rem 0.9rem;
    border: 1px solid rgba(123,158,135,0.3);
    border-radius: 2px;
    margin-top: 1rem;
}
.available-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #7B9E87;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* ── Footer ── */
.footer {
    padding: 2rem 8vw;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.06);
    background: #0C0D11;
}
.footer-left {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: rgba(232,230,223,0.25);
    letter-spacing: 0.08em;
}
.footer-right {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: rgba(232,230,223,0.25);
}
"""


def inject_css() -> None:
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
