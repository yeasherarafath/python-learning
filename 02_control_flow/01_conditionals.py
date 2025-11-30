"""
Control Flow - Conditional Statements
=====================================
This module covers if, elif, and else statements in Python.
"""

# ============================================================================
# BASIC IF STATEMENT
# ============================================================================
print("=== Basic If Statement ===")

age = 18

if age >= 18:
    print(f"Age {age}: You are an adult")

# ============================================================================
# IF-ELSE STATEMENT
# ============================================================================
print("\n=== If-Else Statement ===")

temperature = 25

if temperature > 30:
    print(f"Temperature {temperature}°C: It's hot outside!")
else:
    print(f"Temperature {temperature}°C: It's not too hot")

# ============================================================================
# IF-ELIF-ELSE STATEMENT
# ============================================================================
print("\n=== If-Elif-Else Statement ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

# More examples with different scores
for test_score in [95, 82, 73, 65, 45]:
    if test_score >= 90:
        g = "A"
    elif test_score >= 80:
        g = "B"
    elif test_score >= 70:
        g = "C"
    elif test_score >= 60:
        g = "D"
    else:
        g = "F"
    print(f"  Score {test_score}: Grade {g}")

# ============================================================================
# NESTED IF STATEMENTS
# ============================================================================
print("\n=== Nested If Statements ===")

num = 15

if num > 0:
    print(f"{num} is positive")
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
elif num < 0:
    print(f"{num} is negative")
else:
    print("Number is zero")

# ============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================
print("\n=== Conditional Expressions ===")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# More examples
number = -5
sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
print(f"Number {number} is {sign}")

# ============================================================================
# MULTIPLE CONDITIONS
# ============================================================================
print("\n=== Multiple Conditions ===")

age = 25
has_license = True
has_insurance = True

# Using 'and'
if age >= 18 and has_license:
    print("You can drive!")

# Using 'or'
if age < 18 or not has_license:
    print("You cannot drive")
else:
    print("Driving is allowed")

# Multiple conditions
if age >= 18 and has_license and has_insurance:
    print("All requirements met for driving!")

# ============================================================================
# COMPARING VALUES
# ============================================================================
print("\n=== Comparing Values ===")

a = 10
b = 20
c = 10

# Chained comparisons
print(f"a={a}, b={b}, c={c}")
print(f"a < b < 30: {a < b < 30}")  # True
print(f"a <= c <= b: {a <= c <= b}")  # True

# Comparing strings
name1 = "Alice"
name2 = "Bob"
print(f"\n'{name1}' < '{name2}': {name1 < name2}")  # True (alphabetically)

# ============================================================================
# TRUTHY AND FALSY VALUES
# ============================================================================
print("\n=== Truthy and Falsy Values ===")

# Falsy values
print("Falsy values (evaluate to False):")
falsy_values = [None, 0, 0.0, "", [], {}, set()]
for val in falsy_values:
    print(f"  {repr(val)}: {bool(val)}")

# Truthy values
print("\nTruthy values (evaluate to True):")
truthy_values = [1, -1, "hello", [1, 2], {"a": 1}]
for val in truthy_values:
    print(f"  {repr(val)}: {bool(val)}")

# Practical usage
user_input = ""  # Empty string
if user_input:
    print("User entered something")
else:
    print("User input is empty")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a program that checks if a year is a leap year")
print("2. Create a simple number guessing game feedback system")
print("3. Write a program that determines the largest of three numbers")
print("4. Create a ticket price calculator based on age (child, adult, senior)")
