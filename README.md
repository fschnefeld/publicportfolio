# Portfolio — Analytics & Data Science Lead

A single-page Streamlit portfolio site with a dark, typographic design. Fully custom HTML/CSS — no Streamlit widgets in the UI.

## Stack

- **Python 3.12** via [uv](https://docs.astral.sh/uv/)
- **Streamlit 1.57** as the web framework
- **DM Serif Display / DM Mono / DM Sans** (Google Fonts)
- Custom HTML/CSS layout — no Streamlit columns or widgets

## Project Structure

```
portfolio/
├── app.py                   # Entry point — renders all sections in order
├── pyproject.toml           # uv project config and dependencies
├── uv.lock                  # Locked dependency versions (commit this)
├── .streamlit/
│   └── config.toml          # Server settings and dark theme
├── theme/
│   └── theme.py             # All CSS and inject_css()
├── data_handling/
│   └── content.py           # All editable content (text, stats, projects)
├── pages/
│   ├── nav.py               # Fixed navigation bar
│   ├── hero.py              # Hero section
│   ├── about.py             # About + stat cards
│   ├── expertise.py         # Skills grid
│   ├── projects.py          # Selected projects list
│   ├── philosophy.py        # Quote strip
│   ├── leadership.py        # Leadership principles + team structure
│   ├── contact.py           # Contact links
│   └── footer.py            # Footer
├── api/
│   └── github.py            # GitHub API stub (extend for live stats)
└── AGENTS.md                # Dev and agent instructions
```

## Quick Setup (first time)

```bash
# Clone the repo
git clone <repo-url>
cd portfolio

# Install uv if you don't have it
# https://docs.astral.sh/uv/getting-started/installation/

# Install dependencies and create .venv
uv sync

# Run the app
uv run streamlit run app.py
```

The site will open at [http://localhost:8501](http://localhost:8501).

## Day-to-Day Workflow

See [QUICKSTART.md](QUICKSTART.md) for the full session workflow (branching, running, committing).

## Updating Content

| What | File |
|---|---|
| Stats, skills, projects, team | `data_handling/content.py` |
| Contact email / LinkedIn / GitHub | `pages/contact.py` |
| Section text | `pages/<section>.py` |
| Colors, fonts, spacing | `theme/theme.py` |
| Page title, icon | `app.py` — `st.set_page_config` |
| Section order | `app.py` — render call order |

## Adding a Dependency

```bash
uv add <package-name>
```

Commit both `pyproject.toml` and `uv.lock` together.
