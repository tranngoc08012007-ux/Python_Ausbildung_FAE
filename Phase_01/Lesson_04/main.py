# Lesson 04 - Git Basics
# Learning objectives:
# - Git workflow: add -> commit -> push
# - .gitignore for Python projects
# - Commit Message Convention (feat/fix/docs)

# ============================================================
# Git Workflow - Basic Commands
# ============================================================
# git init                        -> Initialize a new repository
# git add .                       -> Stage all files for commit
# git commit -m "feat: ..."       -> Save a checkpoint
# git push                        -> Upload to GitHub

# ============================================================
# Commit Message Convention
# ============================================================
# feat:     add a new feature
# fix:      fix a bug
# docs:     update documentation or README
# style:    format code (black, flake8) - no logic change
# refactor: restructure code - no new feature
# chore:    minor tasks (.gitignore, dependencies)

# ============================================================
# .gitignore - Files to exclude from Git
# ============================================================
# venv/          -> virtual environment (large, not needed)
# __pycache__/   -> Python cache (auto-generated)
# .env           -> passwords, API keys (sensitive)
# .vscode/       -> personal VS Code settings

# ============================================================
# Example: Commit history of this project
# ============================================================
commits = [
    "7220c8d docs: add README and standard .gitignore",
    "22a0b15 Initial commit - project structure Phase_01-04",
    "6fffd9e feat: restructure Phase_01-04 folder layout",
    "23f7c18 feat: add print, comment, variable examples",
    "0303aad docs: add requirements.txt and requirements-dev.txt",
    "de89f0f fix: correct README.md formatting for Lesson_02",
]

print("=== Git Log - Python_Ausbildung_FAE ===")
for commit in commits:
    print(f"  {commit}")
