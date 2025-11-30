"""
Data Structures - Dictionaries
==============================
This module covers dictionary operations and methods in Python.
"""

# ============================================================================
# CREATING DICTIONARIES
# ============================================================================
print("=== Creating Dictionaries ===")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with elements
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Bob", grade=90, subject="Math")
print(f"Student: {student}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"From pairs: {dict_from_pairs}")

# Using zip
keys = ["x", "y", "z"]
values = [10, 20, 30]
dict_from_zip = dict(zip(keys, values))
print(f"From zip: {dict_from_zip}")

# ============================================================================
# ACCESSING VALUES
# ============================================================================
print("\n=== Accessing Values ===")

person = {"name": "Alice", "age": 25, "city": "New York"}

# Using key
print(f"person['name']: {person['name']}")
print(f"person['age']: {person['age']}")

# Using get() - safer, returns None if key doesn't exist
print(f"person.get('city'): {person.get('city')}")
print(f"person.get('country'): {person.get('country')}")  # Returns None
print(f"person.get('country', 'USA'): {person.get('country', 'USA')}")  # Default value

# ============================================================================
# MODIFYING DICTIONARIES
# ============================================================================
print("\n=== Modifying Dictionaries ===")

person = {"name": "Alice", "age": 25}
print(f"Original: {person}")

# Adding/updating elements
person["city"] = "Boston"
print(f"After adding city: {person}")

person["age"] = 26
print(f"After updating age: {person}")

# Update with multiple key-value pairs
person.update({"country": "USA", "job": "Engineer"})
print(f"After update(): {person}")

# Removing elements
del person["job"]
print(f"After del person['job']: {person}")

popped = person.pop("country")
print(f"After pop('country'): {person}, popped: '{popped}'")

# popitem() - Remove and return last item
last_item = person.popitem()
print(f"After popitem(): {person}, removed: {last_item}")

# ============================================================================
# DICTIONARY METHODS
# ============================================================================
print("\n=== Dictionary Methods ===")

student = {"name": "Bob", "grade": 90, "subject": "Math"}

# keys() - Get all keys
print(f"Keys: {list(student.keys())}")

# values() - Get all values
print(f"Values: {list(student.values())}")

# items() - Get all key-value pairs
print(f"Items: {list(student.items())}")

# copy() - Create a shallow copy
student_copy = student.copy()
print(f"Copy: {student_copy}")

# clear() - Remove all items
student_copy.clear()
print(f"After clear(): {student_copy}")

# setdefault() - Get value or set default
inventory = {"apples": 5, "bananas": 3}
print(f"\nInventory: {inventory}")
print(f"setdefault('apples', 10): {inventory.setdefault('apples', 10)}")  # Returns existing
print(f"setdefault('oranges', 7): {inventory.setdefault('oranges', 7)}")  # Sets new
print(f"After setdefault: {inventory}")

# fromkeys() - Create dict with default values
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"\nfromkeys({keys}, 0): {default_dict}")

# ============================================================================
# ITERATING OVER DICTIONARIES
# ============================================================================
print("\n=== Iterating Over Dictionaries ===")

person = {"name": "Alice", "age": 25, "city": "Boston"}

# Iterate over keys (default)
print("Keys:")
for key in person:
    print(f"  {key}")

# Iterate over values
print("\nValues:")
for value in person.values():
    print(f"  {value}")

# Iterate over key-value pairs
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ============================================================================
# DICTIONARY COMPREHENSIONS
# ============================================================================
print("\n=== Dictionary Comprehensions ===")

# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transforming a dictionary
prices = {"apple": 0.5, "banana": 0.25, "cherry": 0.75}
prices_cents = {k: int(v * 100) for k, v in prices.items()}
print(f"Prices in cents: {prices_cents}")

# Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# ============================================================================
# NESTED DICTIONARIES
# ============================================================================
print("\n=== Nested Dictionaries ===")

students = {
    "student1": {
        "name": "Alice",
        "grades": {"math": 90, "science": 85}
    },
    "student2": {
        "name": "Bob",
        "grades": {"math": 88, "science": 92}
    }
}

print("Students:")
for student_id, info in students.items():
    print(f"  {student_id}:")
    print(f"    Name: {info['name']}")
    print(f"    Math: {info['grades']['math']}")
    print(f"    Science: {info['grades']['science']}")

# Accessing nested values
print(f"\nAlice's math grade: {students['student1']['grades']['math']}")

# ============================================================================
# COMMON PATTERNS
# ============================================================================
print("\n=== Common Patterns ===")

# Counting occurrences
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character count in '{text}': {char_count}")

# Grouping by key
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
by_first_letter = {}
for word in words:
    first = word[0]
    if first not in by_first_letter:
        by_first_letter[first] = []
    by_first_letter[first].append(word)
print(f"Grouped by first letter: {by_first_letter}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a function to merge two dictionaries")
print("2. Create a word frequency counter for a sentence")
print("3. Invert a dictionary (swap keys and values)")
print("4. Create a function to find common keys between two dictionaries")
