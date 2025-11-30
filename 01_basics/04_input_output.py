"""
Python Basics - Input and Output
================================
This module covers input and output operations in Python.
"""

# ============================================================================
# PRINT FUNCTION
# ============================================================================
print("=== Print Function ===")

# Basic print
print("Hello, World!")

# Print multiple items
print("Python", "is", "awesome")

# Print with separator
print("apple", "banana", "cherry", sep=", ")

# Print with end parameter (no newline)
print("Line 1", end=" -> ")
print("Line 2")

# Print with both sep and end
print("A", "B", "C", sep="-", end="!\n")

# ============================================================================
# FORMATTED OUTPUT
# ============================================================================
print("\n=== Formatted Output ===")

name = "Python"
version = 3.11

# Using f-strings
print(f"Language: {name}, Version: {version}")

# Alignment
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")
print(f"{'---':-<10} | {'---':-^10} | {'---':->10}")

# Number formatting
number = 42
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")

price = 49.99
print(f"Price: ${price:.2f}")

large_number = 1000000
print(f"Large number: {large_number:,}")
print(f"Percentage: {0.756:.1%}")

# ============================================================================
# INPUT FUNCTION
# ============================================================================
print("\n=== Input Function (Demo Mode) ===")
print("Note: The input() function waits for user input.")
print("In demo mode, we'll use predefined values.")

# Demo values (in real usage, these would come from input())
demo_name = "Student"
demo_age = "20"
demo_score = "85.5"

print(f"\nDemo input values:")
print(f"  Name: {demo_name}")
print(f"  Age: {demo_age}")
print(f"  Score: {demo_score}")

# Input always returns a string, so we need to convert
age_int = int(demo_age)
score_float = float(demo_score)

print(f"\nAfter type conversion:")
print(f"  Age (int): {age_int}, Type: {type(age_int)}")
print(f"  Score (float): {score_float}, Type: {type(score_float)}")

# ============================================================================
# INPUT EXAMPLES (Commented for demo)
# ============================================================================
print("\n=== Input Examples (Code Samples) ===")
print("""
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")

# Multiple inputs
first = input("First number: ")
second = input("Second number: ")
result = int(first) + int(second)
print(f"Sum: {result}")

# Input with default value
color = input("Favorite color (press Enter for blue): ") or "blue"
print(f"Your favorite color is {color}")
""")

# ============================================================================
# ESCAPE SEQUENCES
# ============================================================================
print("\n=== Escape Sequences ===")

print("Tab:\tSeparated\tText")
print("New line:\nLine 1\nLine 2")
print("Backslash: \\")
print("Quote: \"Hello\"")
print("Single Quote: \'World\'")

# Raw string (no escape processing)
print(r"Raw string: \n\t are not processed")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a program that asks for the user's name and age, then prints a greeting")
print("2. Create a formatted table showing products and their prices")
print("3. Write a simple calculator that takes two numbers and an operator")
