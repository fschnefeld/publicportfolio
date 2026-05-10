# AGENTS.md — Portfolio Project

## Purpose
Single-page Streamlit portfolio for an Analytics & Data Science Lead.
The site renders as one scrollable HTML page with anchor-link navigation.

## How to Run

```bash
# Install dependencies and create .venv
uv sync

# Start the dev server
uv run streamlit run app.py
```

The app will be available at http://localhost:8501.

## Project Structure

```
portfolio/
├── app.py                  # Entry point — DO NOT add content here
├── pyproject.toml          # uv project config
├── .streamlit/config.toml  # Streamlit server + theme settings
├── theme/
│   └── theme.py            # All CSS lives here (inject_css function)
├── data_handling/
│   └── content.py          # All editable content: STATS, SKILLS, PROJECTS, PRINCIPLES, TEAM
├── pages/
│   ├── nav.py              # render_nav()
│   ├── hero.py             # render_hero()
│   ├── about.py            # render_about(stats)
│   ├── expertise.py        # render_expertise(skills)
│   ├── projects.py         # render_projects(projects)
│   ├── philosophy.py       # render_philosophy()
│   ├── leadership.py       # render_leadership(principles, team)
│   ├── contact.py          # render_contact()
│   └── footer.py           # render_footer()
└── api/
    └── github.py           # Stub for future GitHub API integration
```

## Where to Make Changes

| What to change | Where to edit |
|---|---|
| Text, stats, projects, team | `data_handling/content.py` |
| Colours, fonts, spacing | `theme/theme.py` (CSS constants) |
| Section layout / HTML | `pages/<section>.py` |
| Page title, icon, layout | `app.py` (`st.set_page_config`) |
| Section render order | `app.py` (call order at bottom) |
| Contact links | `pages/contact.py` |
| Streamlit server config | `.streamlit/config.toml` |

## pages/ Package Note
The `pages/` directory contains an `__init__.py`, making it a Python package.
This prevents Streamlit from auto-discovering its files as separate app pages
(which would add unwanted sidebar navigation). **Do not remove `__init__.py`.**

## Python Best Practices

### Type hints
Use type hints on all function signatures. Use `TypedDict` for structured data
(see `data_handling/content.py` for examples).

```python
def render_about(stats: list[Stat]) -> None: ...
```

### No bare except
Always catch specific exceptions:

```python
# Bad
try:
    result = fetch()
except:
    pass

# Good
try:
    result = fetch()
except requests.HTTPError as exc:
    st.error(f"Failed to load data: {exc}")
```

### Single responsibility
Each module in `pages/` owns exactly one section. Each `render_*` function
accepts only the data it needs — no global state, no side effects beyond
`st.markdown`.

### No f-string injection of external data
Content in `data_handling/content.py` is internal constants only.
If you ever add user-supplied or API-sourced content, HTML-escape it before
interpolating into f-strings:

```python
import html
safe = html.escape(user_supplied_string)
```

### Imports
Group imports: stdlib → third-party → local. Keep local imports explicit
(`from pages import hero` not `from pages import *`).

### No global mutable state
Do not use `st.session_state` for data that belongs in `content.py`.
Session state is for UI interaction state only.

## Streamlit-Specific Rules

- `st.set_page_config()` must be the **first Streamlit call** in `app.py`.
  Never call it inside section modules.
- All HTML rendering uses `st.markdown(..., unsafe_allow_html=True)`.
- Avoid `st.columns`, `st.expander`, and other Streamlit layout widgets —
  the design uses raw HTML/CSS grids for full visual control.
- Do not add `st.cache_data` / `st.cache_resource` to static content functions.
  Reserve caching for actual I/O (API calls in `api/`).

## Adding a New Section

1. Add data types and constants to `data_handling/content.py`.
2. Create `pages/my_section.py` with a `render_my_section(data)` function.
3. Import and call it in `app.py` at the desired position.
4. Add any new CSS classes to `theme/theme.py`.

## Dependency Management

Add packages via:

```bash
uv add <package>
```

This updates `pyproject.toml` and `uv.lock` atomically. Commit both files.
Do not edit `uv.lock` by hand.
