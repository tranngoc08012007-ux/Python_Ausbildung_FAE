# Lesson 03 — Code Quality Tools: black & flake8

## Overview
This lesson introduces two essential code quality tools used in professional
Python development: `black` (auto-formatter) and `flake8` (linter).

## Tools Covered

| Tool | Type | Purpose |
|------|------|---------|
| `black` | Auto-formatter | Automatically fixes code formatting |
| `flake8` | Linter | Detects PEP 8 violations without fixing |

## What I Learned
- The difference between a linter and an auto-formatter
- How to install black and flake8 via pip
- How to detect formatting errors with flake8
- How to automatically fix formatting with black
- How to configure VS Code to format on save
- How to configure `.flake8` to exclude unnecessary directories

## Project Structure
## Key Commands

```bash
# Install tools
pip install black flake8

# Check for errors (linter)
flake8 main.py

# Auto-fix formatting
black main.py

# Check entire project
flake8 .
black .
```

## Configuration Files

### `.flake8` (project root)
```ini
[flake8]
exclude = myenv, .vscode, __pycache__
max-line-length = 88
```

### `.vscode/settings.json`
```json
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    }
}
```

## PEP 8 — Common Error Codes

| Code | Meaning |
|------|---------|
| E225 | Missing whitespace around operator |
| E231 | Missing whitespace after ',' |
| E302 | Expected 2 blank lines before function |
| W292 | No newline at end of file |

## Key Takeaway
> Write code first, let black handle the formatting.
> Use flake8 as a final check before every git commit.