"""
Python Basics - Operators
=========================
This module covers different types of operators in Python.
"""

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================
print("=== Arithmetic Operators ===")

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================
print("\n=== Comparison Operators ===")

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"Equal (x == y): {x == y}")
print(f"Not Equal (x != y): {x != y}")
print(f"Greater Than (x > y): {x > y}")
print(f"Less Than (x < y): {x < y}")
print(f"Greater or Equal (x >= y): {x >= y}")
print(f"Less or Equal (x <= y): {x <= y}")

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================
print("\n=== Logical Operators ===")

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"AND (p and q): {p and q}")
print(f"OR (p or q): {p or q}")
print(f"NOT p (not p): {not p}")
print(f"NOT q (not q): {not q}")

# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================
print("\n=== Assignment Operators ===")

num = 10
print(f"Initial value: num = {num}")

num += 5  # Same as: num = num + 5
print(f"After num += 5: {num}")

num -= 3  # Same as: num = num - 3
print(f"After num -= 3: {num}")

num *= 2  # Same as: num = num * 2
print(f"After num *= 2: {num}")

num //= 4  # Same as: num = num // 4
print(f"After num //= 4: {num}")

# ============================================================================
# IDENTITY OPERATORS
# ============================================================================
print("\n=== Identity Operators ===")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 is list3: {list1 is list3}")  # True - same object
print(f"list1 is not list2: {list1 is not list2}")

# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================
print("\n=== Membership Operators ===")

fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")

print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Calculate the area of a rectangle with length 7 and width 5")
print("2. Check if 15 is divisible by 3 using modulus operator")
print("3. Use logical operators to check if a number is between 1 and 100")
