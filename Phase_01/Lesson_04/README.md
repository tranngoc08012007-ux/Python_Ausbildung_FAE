# Lesson 04 - Git Basics

## Learning Objectives
After completing this lesson, I can:
- Use the core Git workflow: `git add` → `git commit` → `git push`
- Create and maintain a standard `.gitignore` for Python projects
- Write commit messages following the Conventional Commits standard

---

## Core Concepts

### 1. Git Workflow
```bash
git init                        # Initialize a new repository
git add .                       # Stage all files
git commit -m "feat: ..."       # Save a checkpoint with a message
git push                        # Upload to GitHub
```

### 2. Commit Message Convention

| Type | When to use |
|------|-------------|
| `feat` | Add a new feature |
| `fix` | Fix a bug |
| `docs` | Update documentation or README |
| `style` | Format code (black, flake8) — no logic change |
| `refactor` | Restructure code — no new feature added |
| `chore` | Minor tasks (.gitignore, dependencies) |

**Rules:**
- Always include a type prefix
- Write in English, lowercase
- Keep it short and descriptive

```bash
# ✅ Correct
git commit -m "docs: add README for Lesson 04"
git commit -m "fix: correct .gitignore path"

# ❌ Incorrect
git commit -m "update"
git commit -m "done"
```

### 3. .gitignore — Files to Exclude

```gitignore
venv/           # Virtual environment — large, not needed by others
myenv/
__pycache__/    # Python cache — auto-generated
*.pyc
.env            # Passwords and API keys — sensitive
.vscode/        # Personal VS Code settings
.pytest_cache/
Thumbs.db       # Windows system file
```

---

## Key Rules to Remember
- ⚠️ Always write commit messages in English
- ⚠️ Never commit without a type prefix (`feat:`, `fix:`, `docs:`...)
- ⚠️ Never commit `venv/` or `.env` to GitHub
- ⚠️ Never commit directly to `main` (covered in Lesson 05)

---

## Files in This Lesson
| File | Description |
|------|-------------|
| `main.py` | Git workflow notes and commit history example |
| `README.md` | This file |