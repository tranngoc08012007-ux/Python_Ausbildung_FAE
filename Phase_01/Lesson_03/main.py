# lesson_03_code_quality.py
# Demonstrates the use of black (auto-formatter) and flake8 (linter)
# Part of Phase 01 - Lesson 03: Code Quality Tools


def calculate_sum(first_number: int, second_number: int) -> int:
    """Return the sum of two numbers."""
    return first_number + second_number


def calculate_rectangle_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width


# --- Main execution ---
x = 10
y = 20

result = calculate_sum(x, y)
print(f"Sum: {result}")

area = calculate_rectangle_area(5.0, 3.0)
print(f"Rectangle area: {area}")
