"""
Python Basics - Strings
=======================
This module covers string operations and methods in Python.
"""

# ============================================================================
# STRING CREATION
# ============================================================================
print("=== String Creation ===")

single = 'Hello'
double = "World"
multi = '''This is a
multi-line string'''

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Multi-line:\n{multi}")

# ============================================================================
# STRING INDEXING AND SLICING
# ============================================================================
print("\n=== String Indexing and Slicing ===")

text = "Python Programming"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")

# Indexing
print(f"First character (text[0]): {text[0]}")
print(f"Last character (text[-1]): {text[-1]}")
print(f"Fifth character (text[4]): {text[4]}")

# Slicing
print(f"First 6 characters (text[0:6]): {text[0:6]}")
print(f"Characters from index 7 (text[7:]): {text[7:]}")
print(f"Last 11 characters (text[-11:]): {text[-11:]}")
print(f"Every 2nd character (text[::2]): {text[::2]}")
print(f"Reversed string (text[::-1]): {text[::-1]}")

# ============================================================================
# STRING METHODS
# ============================================================================
print("\n=== String Methods ===")

sample = "  Hello, World!  "
print(f"Original: '{sample}'")

# Case methods
print(f"Upper: '{sample.upper()}'")
print(f"Lower: '{sample.lower()}'")
print(f"Title: '{sample.title()}'")
print(f"Capitalize: '{sample.capitalize()}'")
print(f"Swap case: '{sample.swapcase()}'")

# Whitespace methods
print(f"Strip: '{sample.strip()}'")
print(f"Left strip: '{sample.lstrip()}'")
print(f"Right strip: '{sample.rstrip()}'")

# Search methods
sentence = "Python is awesome and Python is popular"
print(f"\nSentence: '{sentence}'")
print(f"Find 'Python': {sentence.find('Python')}")
print(f"Find 'Java': {sentence.find('Java')}")  # Returns -1 if not found
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'popular': {sentence.endswith('popular')}")

# Replace method
print(f"Replace 'Python' with 'Java': {sentence.replace('Python', 'Java')}")

# Split and Join
words = sentence.split()
print(f"Split into words: {words}")

joined = "-".join(words)
print(f"Joined with '-': {joined}")

# ============================================================================
# STRING FORMATTING
# ============================================================================
print("\n=== String Formatting ===")

name = "Alice"
age = 25
score = 95.5

# f-strings (recommended - Python 3.6+)
print(f"f-string: {name} is {age} years old with score {score}")

# format() method
print("format(): {} is {} years old with score {}".format(name, age, score))

# % operator (older style)
print("%% operator: %s is %d years old with score %.1f" % (name, age, score))

# Formatting numbers
pi = 3.14159265359
print(f"\nPi: {pi}")
print(f"Pi (2 decimals): {pi:.2f}")
print(f"Pi (4 decimals): {pi:.4f}")

number = 1234567
print(f"Number with commas: {number:,}")

# ============================================================================
# STRING CONCATENATION
# ============================================================================
print("\n=== String Concatenation ===")

first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(f"Using +: {full_name}")

# Using join
full_name_join = " ".join([first_name, last_name])
print(f"Using join: {full_name_join}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Create a string with your full name and print each word on a new line")
print("2. Reverse your name string")
print("3. Count how many vowels are in a given sentence")
print("4. Create a formatted string showing your details (name, age, city)")
