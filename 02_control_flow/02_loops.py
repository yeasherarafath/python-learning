"""
Control Flow - Loops
====================
This module covers for loops and while loops in Python.
"""

# ============================================================================
# FOR LOOP BASICS
# ============================================================================
print("=== For Loop Basics ===")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Iterating over a string
print("\nCharacters in 'Python':")
for char in "Python":
    print(f"  {char}")

# ============================================================================
# RANGE FUNCTION
# ============================================================================
print("\n=== Range Function ===")

# range(stop) - 0 to stop-1
print("range(5):", list(range(5)))

# range(start, stop)
print("range(2, 7):", list(range(2, 7)))

# range(start, stop, step)
print("range(0, 10, 2):", list(range(0, 10, 2)))

# Counting backwards
print("range(10, 0, -1):", list(range(10, 0, -1)))

# Using range in a loop
print("\nCounting to 5:")
for i in range(1, 6):
    print(f"  {i}")

# ============================================================================
# WHILE LOOP
# ============================================================================
print("\n=== While Loop ===")

# Basic while loop
count = 1
print("Counting with while:")
while count <= 5:
    print(f"  Count: {count}")
    count += 1

# While with condition
print("\nSum until >= 10:")
total = 0
num = 1
while total < 10:
    total += num
    print(f"  Added {num}, Total: {total}")
    num += 1

# ============================================================================
# BREAK STATEMENT
# ============================================================================
print("\n=== Break Statement ===")

print("Finding first number divisible by 7:")
for i in range(1, 50):
    if i % 7 == 0:
        print(f"  Found: {i}")
        break

print("\nSearching in a list:")
names = ["Alice", "Bob", "Charlie", "David"]
search = "Charlie"
for name in names:
    print(f"  Checking: {name}")
    if name == search:
        print(f"  Found {search}!")
        break

# ============================================================================
# CONTINUE STATEMENT
# ============================================================================
print("\n=== Continue Statement ===")

print("Print odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")

print("\nSkip names starting with 'A':")
names = ["Alice", "Bob", "Amanda", "Charlie"]
for name in names:
    if name.startswith("A"):
        continue
    print(f"  {name}")

# ============================================================================
# ELSE WITH LOOPS
# ============================================================================
print("\n=== Else with Loops ===")

# For-else: else runs if loop completes without break
print("Searching for 'grape' in fruits:")
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "grape":
        print("  Found grape!")
        break
else:
    print("  Grape not found in the list")

# While-else
print("\nCountdown with else:")
n = 3
while n > 0:
    print(f"  {n}...")
    n -= 1
else:
    print("  Liftoff!")

# ============================================================================
# NESTED LOOPS
# ============================================================================
print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication Table (1-5):")
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        row += f"{i*j:4}"
    print(f"  {row}")

# Pattern printing
print("\nTriangle Pattern:")
for i in range(1, 6):
    print("  " + "* " * i)

# ============================================================================
# ENUMERATE AND ZIP
# ============================================================================
print("\n=== Enumerate ===")

colors = ["red", "green", "blue"]
print("Colors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# Starting from 1
print("\nStarting from 1:")
for index, color in enumerate(colors, start=1):
    print(f"  {index}: {color}")

print("\n=== Zip ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("Names and Ages:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# ============================================================================
# LIST COMPREHENSIONS (Preview)
# ============================================================================
print("\n=== List Comprehensions (Preview) ===")

# Traditional way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)
print(f"Squares (traditional): {squares_traditional}")

# List comprehension
squares_comprehension = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares_comprehension}")

# With condition
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a program to find all prime numbers between 1 and 50")
print("2. Create a program that prints the Fibonacci sequence up to n terms")
print("3. Write a program to reverse a string using a loop")
print("4. Create a number pyramid pattern")
