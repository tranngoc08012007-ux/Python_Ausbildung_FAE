# Mini Project 01 — Number Guessing Game

## Description

A simple command-line number guessing game written in Python.

The program generates a random number between **1 and 100**, and the player must guess it within a limited number of attempts. After each guess, the game provides a hint indicating whether the correct number is higher or lower. A score is calculated based on the number of attempts used, and the highest score is tracked during the current game session.

---

## Features

* Random number generation
* Higher / Lower hints after each guess
* Maximum number of attempts
* Score calculation
* High score tracking
* Input validation
* Modular project structure

---

## Skills Applied

* Using the `random` module
* Functions and modular programming
* Loops and conditional statements
* Input validation
* Organizing code into multiple modules (`main.py` and `game.py`)
* Black code formatting
* Flake8 linting
* Conventional Commit messages

---

## Folder Structure

```text
Mini_Project_01/
├── .gitignore
├── requirements.txt
├── game.py
├── main.py
└── README.md
```

---

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/tranngoc08012007-ux/Python_Ausbildung_FAE.git

cd Python_Ausbildung_FAE/Project/Mini_Project_01
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```bash
python -m venv myenv
myenv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> This project only uses the Python standard library, so `requirements.txt` may be empty.

### 4. Run the game

```bash
python main.py
```

---

## Example Output

```text
=============================
  NUMBER GUESSING GAME v2.0
=============================

I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Attempt 1/7: 50
↑ The number is HIGHER than 50.

Attempt 2/7: 75
↓ The number is LOWER than 75.

Attempt 3/7: 63
🎉 Correct! You guessed it in 3 attempts!

Your score: 80
🏆 High score: 80
```

---

## Code Quality

Check formatting:

```bash
black --check .
```

Check linting:

```bash
flake8 .
```

Expected result:

```text
0 errors
0 warnings
```

---

## Future Improvements

* Multiple difficulty levels
* Save the high score to a file
* Play multiple rounds without restarting
* Colored terminal output
* Unit tests with `pytest`
