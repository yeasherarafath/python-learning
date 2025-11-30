"""
Data Structures - Lists
=======================
This module covers list operations and methods in Python.
"""

# ============================================================================
# CREATING LISTS
# ============================================================================
print("=== Creating Lists ===")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# List with mixed types
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

# List from range
numbers = list(range(1, 6))
print(f"From range: {numbers}")

# List from string
chars = list("Python")
print(f"From string: {chars}")

# ============================================================================
# ACCESSING ELEMENTS
# ============================================================================
print("\n=== Accessing Elements ===")

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")

# Indexing
print(f"First element (colors[0]): {colors[0]}")
print(f"Last element (colors[-1]): {colors[-1]}")
print(f"Third element (colors[2]): {colors[2]}")

# Slicing
print(f"First three (colors[:3]): {colors[:3]}")
print(f"Last two (colors[-2:]): {colors[-2:]}")
print(f"Middle (colors[1:4]): {colors[1:4]}")
print(f"Every other (colors[::2]): {colors[::2]}")
print(f"Reversed (colors[::-1]): {colors[::-1]}")

# ============================================================================
# MODIFYING LISTS
# ============================================================================
print("\n=== Modifying Lists ===")

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Changing elements
numbers[0] = 10
print(f"After numbers[0] = 10: {numbers}")

# Changing a range
numbers[1:3] = [20, 30]
print(f"After numbers[1:3] = [20, 30]: {numbers}")

# ============================================================================
# LIST METHODS
# ============================================================================
print("\n=== List Methods ===")

# append() - Add element to end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# insert() - Add element at specific position
fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")

# extend() - Add multiple elements
fruits.extend(["date", "elderberry"])
print(f"After extend(['date', 'elderberry']): {fruits}")

# remove() - Remove first occurrence
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# pop() - Remove and return element
popped = fruits.pop()
print(f"After pop(): {fruits}, popped: '{popped}'")

popped_first = fruits.pop(0)
print(f"After pop(0): {fruits}, popped: '{popped_first}'")

# index() - Find index of element
numbers = [10, 20, 30, 20, 40]
print(f"\nNumbers: {numbers}")
print(f"Index of 20: {numbers.index(20)}")

# count() - Count occurrences
print(f"Count of 20: {numbers.count(20)}")

# sort() - Sort in place
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nUnsorted: {nums}")
nums.sort()
print(f"Sorted: {nums}")
nums.sort(reverse=True)
print(f"Sorted descending: {nums}")

# sorted() - Return new sorted list
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(f"\nOriginal unchanged: {original}")
print(f"Sorted copy: {sorted_copy}")

# reverse() - Reverse in place
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(f"Reversed: {nums}")

# copy() - Create a shallow copy
original = [1, 2, 3]
copy_list = original.copy()
print(f"\nOriginal: {original}")
print(f"Copy: {copy_list}")

# clear() - Remove all elements
copy_list.clear()
print(f"After clear(): {copy_list}")

# ============================================================================
# LIST OPERATIONS
# ============================================================================
print("\n=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"list1 + list2: {combined}")

# Repetition
repeated = [0] * 5
print(f"[0] * 5: {repeated}")

# Membership
print(f"2 in list1: {2 in list1}")
print(f"10 in list1: {10 in list1}")

# Length
print(f"len(list1): {len(list1)}")

# Min, Max, Sum
numbers = [5, 2, 8, 1, 9]
print(f"\nNumbers: {numbers}")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"sum: {sum(numbers)}")

# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================
print("\n=== List Comprehensions ===")

# Basic comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Transforming strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Nested comprehension (flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Conditional expression
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"Absolute values: {abs_values}")

# ============================================================================
# NESTED LISTS
# ============================================================================
print("\n=== Nested Lists (2D Lists) ===")

# Creating a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Accessing elements
print(f"\nElement at row 1, col 2: {matrix[1][2]}")

# Creating a 3x3 matrix with comprehension
zeros = [[0 for _ in range(3)] for _ in range(3)]
print(f"\n3x3 Zeros: {zeros}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a function to remove duplicates from a list while preserving order")
print("2. Create a function to rotate a list by n positions")
print("3. Find the second largest number in a list")
print("4. Merge two sorted lists into a single sorted list")
