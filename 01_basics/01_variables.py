"""
Python Basics - Variables and Data Types
=========================================
This module covers the fundamental concepts of variables and data types in Python.
"""

# ============================================================================
# VARIABLES
# ============================================================================
# Variables are containers for storing data values.
# Python has no command for declaring a variable - it's created when you assign a value.

# Example: Creating variables
name = "Yeasher"  # String variable
age = 20  # Integer variable
height = 5.8  # Float variable
is_student = True  # Boolean variable

# Printing variables
print("=== Variables Demo ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# ============================================================================
# DATA TYPES
# ============================================================================
# Python has several built-in data types

# 1. Numeric Types
integer_num = 10  # int
float_num = 10.5  # float
complex_num = 3 + 4j  # complex

print("\n=== Numeric Types ===")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# 2. String Type
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line
string"""

print("\n=== String Type ===")
print(f"Single Quote: {single_quote}")
print(f"Double Quote: {double_quote}")
print(f"Multi-line: {multi_line}")

# 3. Boolean Type
is_true = True
is_false = False

print("\n=== Boolean Type ===")
print(f"True value: {is_true}")
print(f"False value: {is_false}")

# 4. None Type
nothing = None

print("\n=== None Type ===")
print(f"None value: {nothing}")

# ============================================================================
# TYPE CONVERSION
# ============================================================================
# Converting between data types

print("\n=== Type Conversion ===")

# String to Integer
str_num = "100"
converted_int = int(str_num)
print(f"String '{str_num}' to Integer: {converted_int}")

# Integer to String
num = 42
converted_str = str(num)
print(f"Integer {num} to String: '{converted_str}'")

# Integer to Float
int_val = 10
float_val = float(int_val)
print(f"Integer {int_val} to Float: {float_val}")

# Float to Integer (truncates decimal)
float_val2 = 10.9
int_val2 = int(float_val2)
print(f"Float {float_val2} to Integer: {int_val2}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Create variables to store your name, age, and favorite number")
print("2. Print the type of each variable you created")
print("3. Convert a string '25.5' to a float and then to an integer")
