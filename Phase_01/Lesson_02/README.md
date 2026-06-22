# Lesson_02: Virtual Environment & pip

## What I Learned

In this lesson, I learned how to create an isolated Python development environment using **venv** and manage project dependencies using **pip**.

The main goal is to keep each project independent by using separate environments and controlling the required packages.

---

## Key Concepts

## Virtual Environment (venv)

A **virtual environment** is a self-contained directory that contains a specific Python interpreter and installed packages.

It allows each project to have its own dependencies, preventing conflicts between different projects that may require different package versions.

Example:

- Project A → uses `Django 4.x`
- Project B → uses `Django 5.x`

Both projects can run independently with their own environments.

---

## pip & PyPI

**pip** is Python's package installer.

It allows developers to install, update, and manage external Python libraries.

Packages are downloaded from **PyPI (Python Package Index)** and installed into the currently active virtual environment.

Example:

```bash
pip install requests
```

---

## requirements.txt vs requirements-dev.txt

| File | Contains | Purpose |
|---|---|---|
| `requirements.txt` | Production dependencies (e.g. `requests`) | Required to run the application |
| `requirements-dev.txt` | Development tools (e.g. `pytest`) | Only needed during development and testing |

---

# Commands Used

## Create and activate virtual environment

```bash
# Create virtual environment
python -m venv myenv

# Activate on Windows
myenv\Scripts\activate

# Exit virtual environment
deactivate
```

---

## Install packages

```bash
# Install a package
pip install <package-name>

# Install a specific version
pip install <package-name>==<version>
```

Example:

```bash
pip install requests==2.32.3
```

---

## Manage dependencies

```bash
# List all installed packages
pip freeze

# Save installed packages
pip freeze > requirements.txt

# Recreate environment from file
pip install -r requirements.txt
```

---

# Project Structure

```
Lesson_02/
│
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

---

# Notes

- The `myenv/` folder is excluded from Git using `.gitignore`.
- Never push the virtual environment folder to GitHub because it is machine-specific and can be recreated.
- `requirements.txt` and `requirements-dev.txt` should be committed so other developers can reproduce the same environment.
- Dependencies should be installed inside the virtual environment, not globally.

---

# Problem Solved

During setup, I encountered a **PSSecurityException** on Windows when activating the virtual environment.

The issue was resolved by changing the PowerShell execution policy to:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

This allowed locally created scripts, such as the virtual environment activation script, to run correctly.

---

# Summary
After completing this lesson, I can:

- Create and manage Python virtual environments
- Install and control project dependencies
- Use `requirements.txt` for environment reproduction
- Understand basic Python project setup practices
