"""
Functions - Basics
==================
This module covers function definition, parameters, and return values in Python.
"""

# ============================================================================
# BASIC FUNCTION DEFINITION
# ============================================================================
print("=== Basic Function Definition ===")


def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")


# Calling the function
greet()


def greet_person(name):
    """A function that greets a specific person."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")

# ============================================================================
# FUNCTION WITH RETURN VALUE
# ============================================================================
print("\n=== Function with Return Value ===")


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


result = add(5, 3)
print(f"add(5, 3) = {result}")


def square(n):
    """Return the square of a number."""
    return n ** 2


print(f"square(4) = {square(4)}")


def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


area = calculate_area(5, 3)
print(f"calculate_area(5, 3) = {area}")

# ============================================================================
# MULTIPLE RETURN VALUES
# ============================================================================
print("\n=== Multiple Return Values ===")


def get_min_max(numbers):
    """Return both minimum and maximum of a list."""
    return min(numbers), max(numbers)


nums = [5, 2, 8, 1, 9]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {minimum}, Max: {maximum}")


def divide_with_remainder(a, b):
    """Return quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide_with_remainder(17, 5)
print(f"17 / 5: Quotient = {q}, Remainder = {r}")

# ============================================================================
# DEFAULT PARAMETERS
# ============================================================================
print("\n=== Default Parameters ===")


def greet_with_message(name, message="Hello"):
    """Greet with a customizable message."""
    print(f"{message}, {name}!")


greet_with_message("Alice")  # Uses default message
greet_with_message("Bob", "Good morning")  # Custom message


def power(base, exponent=2):
    """Calculate power with default exponent of 2."""
    return base ** exponent


print(f"power(3) = {power(3)}")  # 3^2 = 9
print(f"power(3, 3) = {power(3, 3)}")  # 3^3 = 27
print(f"power(2, 10) = {power(2, 10)}")  # 2^10 = 1024

# ============================================================================
# KEYWORD ARGUMENTS
# ============================================================================
print("\n=== Keyword Arguments ===")


def describe_person(name, age, city):
    """Describe a person with their details."""
    print(f"{name} is {age} years old and lives in {city}")


# Positional arguments
describe_person("Alice", 25, "New York")

# Keyword arguments (any order)
describe_person(city="London", name="Bob", age=30)

# Mixed (positional first, then keyword)
describe_person("Charlie", city="Paris", age=35)

# ============================================================================
# *ARGS - VARIABLE POSITIONAL ARGUMENTS
# ============================================================================
print("\n=== *args - Variable Positional Arguments ===")


def sum_all(*numbers):
    """Sum all given numbers."""
    return sum(numbers)


print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


def print_all(*args):
    """Print all arguments."""
    for i, arg in enumerate(args, 1):
        print(f"  Arg {i}: {arg}")


print("Printing all arguments:")
print_all("apple", "banana", 42, True)

# ============================================================================
# **KWARGS - VARIABLE KEYWORD ARGUMENTS
# ============================================================================
print("\n=== **kwargs - Variable Keyword Arguments ===")


def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("Person info:")
print_info(name="Alice", age=25, city="New York", job="Engineer")


def build_profile(first, last, **other_info):
    """Build a user profile dictionary."""
    profile = {"first_name": first, "last_name": last}
    profile.update(other_info)
    return profile


profile = build_profile("John", "Doe", age=30, email="john@example.com")
print(f"\nProfile: {profile}")

# ============================================================================
# COMBINING *ARGS AND **KWARGS
# ============================================================================
print("\n=== Combining *args and **kwargs ===")


def flexible_function(*args, **kwargs):
    """A function that accepts any number of positional and keyword arguments."""
    print(f"  Positional args: {args}")
    print(f"  Keyword args: {kwargs}")


print("Calling flexible_function:")
flexible_function(1, 2, 3, name="Alice", age=25)

# ============================================================================
# DOCSTRINGS
# ============================================================================
print("\n=== Docstrings ===")


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight: Weight in kilograms
        height: Height in meters

    Returns:
        BMI value as a float

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return round(weight / (height ** 2), 2)


# Accessing docstring
print(f"Function docstring:\n{calculate_bmi.__doc__}")
print(f"\nBMI for 70kg, 1.75m: {calculate_bmi(70, 1.75)}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a function that checks if a number is prime")
print("2. Create a function that returns the factorial of a number")
print("3. Write a function that counts vowels in a string")
print("4. Create a function that reverses a string without using slicing")
