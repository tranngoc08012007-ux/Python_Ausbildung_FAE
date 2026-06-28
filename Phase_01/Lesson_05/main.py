# Lesson 05 - Git Branch & Pull Request
# Phase 1 - Professional Development Environment
#
# ============================================================
# CORE CONCEPT
# ============================================================
# main   = finished product (always clean, always runnable)
# branch = workspace (experiment, code, fix — then merge)
#
# Rule: NEVER commit directly to main.
#       Always: branch → code → review → merge
#
# ============================================================
# BRANCH COMMANDS
# ============================================================
# git branch                                → list all branches (* = current)
# git checkout -b feat/branch-name          → create new branch and switch to it
# git checkout main                         → switch back to main
# git branch -m new-name                    → rename current branch
# git branch -d feat/branch-name            → delete local branch
# git push origin --delete feat/branch-name → delete remote branch (GitHub)
#
# ============================================================
# PUSH & PULL REQUEST
# ============================================================
# git push --set-upstream origin feat/branch-name → push new branch to GitHub (first time)
# git push                                         → push after first time
#
# Pull Request (PR) = request to merge branch into main
# → open PR on GitHub → review (by teammate or AI) → merge or close
# → after merge: delete branch (no longer needed)
#
# ============================================================
# FULL WORKFLOW
# ============================================================
# 1. git checkout main
# 2. git pull                               → get latest main
# 3. git checkout -b feat/lesson-xx-topic   → create branch
# 4. code → black → flake8 → commit
# 5. git push --set-upstream origin feat/lesson-xx-topic
# 6. open PR on GitHub → review → merge
# 7. git checkout main → git pull           → update local main
# 8. git branch -d feat/lesson-xx-topic     → clean up