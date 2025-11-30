"""
Data Structures - Tuples and Sets
=================================
This module covers tuple and set operations in Python.
"""

# ============================================================================
# TUPLES - IMMUTABLE SEQUENCES
# ============================================================================
print("=== Creating Tuples ===")

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with elements
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# Tuple without parentheses (packing)
point = 1, 2, 3
print(f"Point (packed): {point}")

# Single element tuple (needs comma)
single = (5,)
print(f"Single element tuple: {single}, type: {type(single)}")

not_tuple = (5)
print(f"Not a tuple: {not_tuple}, type: {type(not_tuple)}")

# Tuple from other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
print(f"From list: {from_list}")
print(f"From string: {from_string}")

# ============================================================================
# TUPLE OPERATIONS
# ============================================================================
print("\n=== Tuple Operations ===")

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Colors: {colors}")

# Indexing and slicing
print(f"First element: {colors[0]}")
print(f"Last element: {colors[-1]}")
print(f"Slice [1:3]: {colors[1:3]}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"\nNumbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(f"Concatenation: {tuple1 + tuple2}")
print(f"Repetition: {tuple1 * 2}")

# Length, min, max
print(f"Length: {len(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")

# ============================================================================
# TUPLE UNPACKING
# ============================================================================
print("\n=== Tuple Unpacking ===")

# Basic unpacking
point = (10, 20, 30)
x, y, z = point
print(f"Point: {point}")
print(f"x={x}, y={y}, z={z}")

# Swapping values
a, b = 1, 2
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
print(f"\nExtended unpacking:")
print(f"first: {first}, middle: {middle}, last: {last}")

head, *tail = (1, 2, 3, 4, 5)
print(f"head: {head}, tail: {tail}")

# ============================================================================
# TUPLE AS DICTIONARY KEYS
# ============================================================================
print("\n=== Tuple as Dictionary Keys ===")

# Tuples can be dictionary keys (unlike lists)
locations = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north"
}

print(f"Locations: {locations}")
print(f"Location at (0, 0): {locations[(0, 0)]}")

# ============================================================================
# NAMED TUPLES (from collections)
# ============================================================================
print("\n=== Named Tuples ===")

from collections import namedtuple

# Create a named tuple class
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
alice = Person("Alice", 25, "New York")
bob = Person(name="Bob", age=30, city="Boston")

print(f"Alice: {alice}")
print(f"Bob: {bob}")
print(f"Alice's name: {alice.name}")
print(f"Bob's age: {bob.age}")

# Convert to dictionary
print(f"Alice as dict: {alice._asdict()}")

# ============================================================================
# SETS - UNIQUE UNORDERED COLLECTIONS
# ============================================================================
print("\n=== Creating Sets ===")

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Set from list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(f"From list with duplicates: {numbers}")
print(f"Set (unique): {unique}")

# ============================================================================
# SET METHODS
# ============================================================================
print("\n=== Set Methods ===")

colors = {"red", "green", "blue"}
print(f"Colors: {colors}")

# add() - Add single element
colors.add("yellow")
print(f"After add('yellow'): {colors}")

# update() - Add multiple elements
colors.update(["purple", "orange"])
print(f"After update(['purple', 'orange']): {colors}")

# remove() - Remove element (raises error if not found)
colors.remove("orange")
print(f"After remove('orange'): {colors}")

# discard() - Remove element (no error if not found)
colors.discard("pink")  # No error
print(f"After discard('pink'): {colors}")

# pop() - Remove and return arbitrary element
popped = colors.pop()
print(f"After pop(): {colors}, popped: '{popped}'")

# ============================================================================
# SET OPERATIONS
# ============================================================================
print("\n=== Set Operations ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union - all elements from both sets
print(f"Union (A | B): {set_a | set_b}")
print(f"Union method: {set_a.union(set_b)}")

# Intersection - elements in both sets
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Intersection method: {set_a.intersection(set_b)}")

# Difference - elements in A but not in B
print(f"Difference (A - B): {set_a - set_b}")
print(f"Difference (B - A): {set_b - set_a}")
print(f"Difference method: {set_a.difference(set_b)}")

# Symmetric difference - elements in either but not both
print(f"Symmetric diff (A ^ B): {set_a ^ set_b}")
print(f"Symmetric diff method: {set_a.symmetric_difference(set_b)}")

# ============================================================================
# SET COMPARISONS
# ============================================================================
print("\n=== Set Comparisons ===")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2, 3}

print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Set Z: {set_z}")

# Subset
print(f"X is subset of Y: {set_x.issubset(set_y)}")
print(f"X <= Y: {set_x <= set_y}")

# Superset
print(f"Y is superset of X: {set_y.issuperset(set_x)}")
print(f"Y >= X: {set_y >= set_x}")

# Equality
print(f"X == Z: {set_x == set_z}")

# Disjoint (no common elements)
set_w = {10, 20, 30}
print(f"X and W are disjoint: {set_x.isdisjoint(set_w)}")

# ============================================================================
# FROZEN SETS (IMMUTABLE)
# ============================================================================
print("\n=== Frozen Sets ===")

frozen = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen}")
print(f"Type: {type(frozen)}")

# Can use as dictionary key
set_dict = {frozen: "my frozen set"}
print(f"Dictionary with frozenset key: {set_dict}")

# ============================================================================
# SET COMPREHENSIONS
# ============================================================================
print("\n=== Set Comprehensions ===")

# Basic comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Find common elements between three lists using sets")
print("2. Remove duplicates from a list while preserving order")
print("3. Check if two strings are anagrams using sets")
print("4. Create a function to find all unique characters in a string")
