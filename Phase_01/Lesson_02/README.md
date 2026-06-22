Lesson 02 — Virtual Environment & pip

What I Learned

How to create an isolated development environment using venv and manage project dependencies using pip.

Key Concepts

Virtual Environment (venv)

A self-contained directory that holds a specific Python installation and packages, isolated from the global Python on the machine. Each project gets its own environment to avoid version conflicts between projects.

pip & PyPI

pip is Python's package installer. It downloads libraries from PyPI (Python Package Index) and installs them into the active environment.

requirements.txt vs requirements-dev.txt

FileContainsPurposerequirements.txtProduction dependencies (e.g. requests)Required to run the apprequirements-dev.txtDevelopment-only tools (e.g. pytest)Only needed during development

Commands Used

bash# Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate       # Windows
deactivate                   # Exit venv

# Install packages
pip install <package-name>
pip install <package>==<version>

# Manage dependencies
pip freeze                           # List all installed packages
pip install -r requirements.txt      # Recreate environment from file

Notes


myenv/ is excluded from Git via .gitignore — never push the venv folder.
requirements.txt and requirements-dev.txt must be committed so others can reproduce the exact environment.
Encountered and resolved PSSecurityException on Windows by setting PowerShell execution policy to RemoteSigned for the current user.