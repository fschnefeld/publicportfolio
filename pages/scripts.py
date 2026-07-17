import streamlit as st

_JS = r"""
(function () {
  if (window.__portfolioInit) return;
  window.__portfolioInit = true;

  function init() {
    // ── Scroll animations ──
    const sections = document.querySelectorAll('.animate-section');
    if (!sections.length) { setTimeout(init, 100); return; }

    const fadeObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          fadeObserver.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    sections.forEach(function(el) { fadeObserver.observe(el); });

    // ── Active nav highlight ──
    const navLinks = document.querySelectorAll('.nav-links a[data-section]');
    if (navLinks.length) {
      const navObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) {
            navLinks.forEach(function(a) { a.classList.remove('active'); });
            const link = document.querySelector(
              '.nav-links a[data-section="' + e.target.id + '"]'
            );
            if (link) link.classList.add('active');
          }
        });
      }, { threshold: 0, rootMargin: '-40% 0px -55% 0px' });
      document.querySelectorAll('section[id]').forEach(function(el) {
        navObserver.observe(el);
      });
    }

    // ── Stat count-up ──
    const countObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseInt(el.dataset.target, 10);
        const suffix = el.dataset.suffix || '';
        const start = performance.now();
        const dur = 1200;
        (function step(now) {
          const t = Math.min((now - start) / dur, 1);
          const eased = 1 - Math.pow(1 - t, 3);
          el.textContent = Math.round(target * eased) + suffix;
          if (t < 1) requestAnimationFrame(step);
        })(start);
        countObserver.unobserve(el);
      });
    }, { threshold: 0.5 });
    document.querySelectorAll('.stat-num[data-target]').forEach(function(el) {
      countObserver.observe(el);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""


def render_scripts() -> None:
    st.markdown(f"<script>{_JS}</script>", unsafe_allow_html=True)
