# Lesson 05 - Git Branch & Pull Request

## Overview
This lesson covers professional Git branch workflow used in every German Betrieb.
No Python code — all practice is done in the terminal and on GitHub.

## What I Learned
- The difference between `main` and a branch
- How to create, switch, rename, and delete branches
- How to push a branch to GitHub
- How to open, review, and close a Pull Request (PR)

## Key Concepts

**main = finished product**
- Always clean, always runnable
- Never commit directly to main

**branch = workspace**
- Where all coding, fixing, and experimenting happens
- Merged into main only after review

**Pull Request (PR)**
- A request to merge a branch into main
- Allows review before code enters main
- Can be merged or closed without merging

## Branch Workflow
## Commands Reference

| Command | Description |
|---|---|
| `git branch` | List all branches |
| `git checkout -b feat/name` | Create and switch to new branch |
| `git checkout main` | Switch back to main |
| `git branch -m new-name` | Rename current branch |
| `git branch -d feat/name` | Delete local branch |
| `git push --set-upstream origin feat/name` | Push new branch to GitHub |
| `git push origin --delete feat/name` | Delete remote branch |

## What I Practiced
- Created branch `feat/lesson-05-branch-demo`
- Added `demo.py` and committed on the branch
- Pushed branch to GitHub
- Opened and closed a Pull Request without merging