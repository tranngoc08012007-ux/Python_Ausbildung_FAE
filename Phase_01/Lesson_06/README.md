# Lesson 06 — Variables & Data Types

## Overview

This lesson introduces the fundamental concepts of variables and built-in data types in Python. It also covers basic arithmetic operations, user input, type casting, and formatted output using f-strings.

---

## Topics Covered

- Variable declaration
- Built-in data types
  - `int`
  - `float`
  - `str`
  - `bool`
  - `None`
- Checking data types with `type()`
- Basic arithmetic operators
  - `+`
  - `/`
  - `//`
  - `%`
- User input with `input()`
- Type casting using `int()`
- Advanced `print()` options
  - `sep`
  - `end`
- Formatted strings (f-strings)

---

## Project Structure

```text
lesson-06/
├── main.py
└── README.md
```

---

## What This Program Demonstrates

### 1. Variables and Data Types

Create variables using Python's most common built-in data types.

```python
name = "Ngoc"
age = 18
height = 1.75
is_graduated = False
note = None
```

---

### 2. Checking Data Types

Use `type()` to determine the data type of a variable.

Example:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

---

### 3. Arithmetic Operations

Perform basic mathematical calculations.

Example:

```python
age + 5
age / 3
age // 3
age % 3
```

Concepts covered:

- Addition
- Division
- Floor division
- Modulus

---

### 4. User Input

Receive input from the user.

```python
user_age = input("Enter your age: ")
```

**Important**

`input()` always returns a string.

---

### 5. Type Casting

Convert a string into an integer before performing calculations.

```python
age_int = int(user_age)
```

---

### 6. Advanced `print()`

Customize output using `sep` and `end`.

Example:

```python
print("Python", "FAE", "2026", sep=" - ")
```

Output:

```text
Python - FAE - 2026
```

Example:

```python
print("Processing", end="...")
print("Done!")
```

Output:

```text
Processing...Done!
```

---

### 7. f-Strings

Use f-strings to create readable formatted output.

```python
print(f"My name is {name}.")
```

---

## Learning Objectives

After completing this lesson, you should be able to:

- Declare variables
- Understand Python's basic data types
- Inspect data types using `type()`
- Perform arithmetic calculations
- Accept user input
- Convert between data types
- Format output using f-strings
- Customize `print()` behavior

---

## How to Run

```bash
python main.py
```

---

## Expected Skills

- Python fundamentals
- Variables
- Data types
- Console input/output
- Basic arithmetic
- Type conversion
- String formatting

---

## Author

**Tran Ngoc**