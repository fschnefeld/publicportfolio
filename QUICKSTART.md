# Quickstart — Every Dev Session

A step-by-step guide for starting work on the portfolio, from a clean state to running app.

---

## 1. Get onto main and pull latest

```bash
git checkout main
git pull origin main
```

Always start from an up-to-date main. Never work directly on main.

---

## 2. Create a feature branch

Name branches by what you're changing:

```bash
# Examples
git checkout -b update/contact-links
git checkout -b add/new-project-entry
git checkout -b fix/hero-layout
git checkout -b style/typography-tweak
```

Branch naming convention: `<type>/<short-description>`
Types: `update`, `add`, `fix`, `style`, `refactor`

---

## 3. Sync dependencies

Run this every session in case `uv.lock` changed since your last pull:

```bash
uv sync
```

This is fast if nothing changed. It ensures your `.venv` matches the lockfile exactly.

---

## 4. Run the app

```bash
uv run streamlit run app.py
```

The site opens at [http://localhost:8501](http://localhost:8501).

Streamlit hot-reloads on file save — you don't need to restart between edits.

---

## 5. Make your changes

| What to edit | Where |
|---|---|
| Text, stats, projects, team | `data_handling/content.py` |
| Contact links | `pages/contact.py` |
| CSS / visual design | `theme/theme.py` |
| Section HTML | `pages/<section>.py` |
| Page config (title, icon) | `app.py` |

---

## 6. Commit your work

Stage and commit in logical chunks — one concern per commit:

```bash
# Check what changed
git status
git diff

# Stage specific files (avoid git add -A)
git add data_handling/content.py
git commit -m "update: add new forecasting project entry"

# Or stage multiple related files
git add pages/contact.py pages/hero.py
git commit -m "update: replace placeholder contact details"
```

Good commit message format: `<type>: <what changed>`
Types: `update`, `add`, `fix`, `style`, `refactor`, `chore`

---

## 7. Push your branch

```bash
git push -u origin <your-branch-name>
```

The `-u` flag links your local branch to the remote — subsequent pushes just need `git push`.

---

## 8. Merge back to main when done

```bash
git checkout main
git pull origin main
git merge <your-branch-name>
git push origin main
```

Or open a pull request if you want a review step before merging.

---

## Common Commands Cheatsheet

```bash
# See all branches
git branch -a

# See what's changed since your last commit
git status
git diff

# Discard uncommitted changes to a single file
git checkout -- pages/contact.py

# Undo the last commit (keep changes staged)
git reset --soft HEAD~1

# See recent commits
git log --oneline -10

# Add a new Python dependency
uv add <package>

# Remove a dependency
uv remove <package>

# Check which Python / Streamlit version is active
uv run python --version
uv run streamlit --version
```

---

## Troubleshooting

**Port already in use:**
```bash
uv run streamlit run app.py --server.port 8502
```

**Module not found after pulling:**
```bash
uv sync
```

**Streamlit not hot-reloading:**
Save the file again, or press `R` in the browser while the app is focused.

**`.venv` is broken or corrupt:**
```bash
rm -rf .venv
uv sync
```
