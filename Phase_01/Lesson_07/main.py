"""
Lesson 07: Strings
Part 1: String Slicing

Topics:
- Basic slicing
- Omitting start/stop
- Negative indexing
- Step
- Reversing a string

Author: Tran Ngoc
"""

# ==========================================================
# Part 1: String Slicing
# ==========================================================

text = "Fachinformatiker"

# --- 1. Basic Slicing -------------------------------------

# Syntax:
# string[start:stop]
# Includes start index, excludes stop index.

print(text[0:5])  # "Fachi"


# --- 2. Omitting Start or Stop ----------------------------

# If start is omitted, Python starts from the beginning.
print(text[:4])  # "Fach"

# If stop is omitted, Python goes to the end.
print(text[4:])  # "informatiker"


# --- 3. Negative Indexing ---------------------------------

# Negative indexes count from the end of the string.
print(text[-4:])  # "iker"


# --- 4. Using Step ----------------------------------------

# Syntax:
# string[start:stop:step]

# Take every second character.
print(text[::2])


# --- 5. Reversing a String --------------------------------

# A step of -1 reverses the string.
print(text[::-1])  # "rekitamrofnihhcaf" (reversed)
