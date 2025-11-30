"""
Functions - Advanced Concepts
=============================
This module covers lambda functions, scope, recursion, and decorators.
"""

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================
print("=== Lambda Functions ===")

# Regular function
def square_regular(x):
    return x ** 2


# Lambda function
square_lambda = lambda x: x ** 2

print(f"Regular function: square_regular(5) = {square_regular(5)}")
print(f"Lambda function: square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Lambda add(3, 4) = {add(3, 4)}")

# Using lambda with built-in functions
print("\n--- Lambda with sorted() ---")
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(f"Original: {students}")

# Sort by score
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"Sorted by score: {sorted_by_score}")

# Sort by score descending
sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted descending: {sorted_desc}")

# Using lambda with map()
print("\n--- Lambda with map() ---")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Using lambda with filter()
print("\n--- Lambda with filter() ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# ============================================================================
# SCOPE - LOCAL AND GLOBAL
# ============================================================================
print("\n=== Scope - Local and Global ===")

global_var = "I am global"


def demonstrate_scope():
    local_var = "I am local"
    print(f"  Inside function - global_var: {global_var}")
    print(f"  Inside function - local_var: {local_var}")


demonstrate_scope()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variable
counter = 0


def increment():
    global counter
    counter += 1
    print(f"  Counter inside function: {counter}")


print("\nUsing global keyword:")
print(f"Counter before: {counter}")
increment()
increment()
print(f"Counter after: {counter}")

# ============================================================================
# ENCLOSING SCOPE (NESTED FUNCTIONS)
# ============================================================================
print("\n=== Enclosing Scope ===")


def outer_function():
    outer_var = "outer"

    def inner_function():
        inner_var = "inner"
        print(f"  Inner can access outer_var: {outer_var}")
        print(f"  Inner has its own inner_var: {inner_var}")

    inner_function()
    # print(inner_var)  # This would cause an error


outer_function()


# Using nonlocal
def counter_factory():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


print("\nUsing nonlocal:")
my_counter = counter_factory()
print(f"Count: {my_counter()}")  # 1
print(f"Count: {my_counter()}")  # 2
print(f"Count: {my_counter()}")  # 3

# ============================================================================
# RECURSION
# ============================================================================
print("\n=== Recursion ===")


# Factorial using recursion
def factorial(n):
    """Calculate factorial of n using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Factorial:")
for i in range(1, 6):
    print(f"  {i}! = {factorial(i)}")


# Fibonacci using recursion
def fibonacci(n):
    """Return nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nFibonacci sequence (first 10):")
fib_sequence = [fibonacci(i) for i in range(10)]
print(f"  {fib_sequence}")


# Sum of list using recursion
def recursive_sum(lst):
    """Sum a list using recursion."""
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


numbers = [1, 2, 3, 4, 5]
print(f"\nRecursive sum of {numbers}: {recursive_sum(numbers)}")

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================
print("\n=== Higher-Order Functions ===")


# Function that takes a function as argument
def apply_twice(func, value):
    """Apply a function twice to a value."""
    return func(func(value))


def add_five(x):
    return x + 5


result = apply_twice(add_five, 10)
print(f"apply_twice(add_five, 10) = {result}")  # (10+5)+5 = 20


# Function that returns a function
def multiplier(n):
    """Return a function that multiplies by n."""
    def multiply(x):
        return x * n
    return multiply


double = multiplier(2)
triple = multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# ============================================================================
# SIMPLE DECORATORS
# ============================================================================
print("\n=== Simple Decorators ===")


def my_decorator(func):
    """A simple decorator that adds behavior before and after a function."""
    def wrapper():
        print("  Before function call")
        func()
        print("  After function call")
    return wrapper


@my_decorator
def say_hello():
    print("  Hello!")


print("Calling decorated function:")
say_hello()


# Decorator with arguments
def decorator_with_args(func):
    """Decorator that works with function arguments."""
    def wrapper(*args, **kwargs):
        print(f"  Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"  Result: {result}")
        return result
    return wrapper


@decorator_with_args
def add_numbers(a, b):
    return a + b


print("\nDecorator with arguments:")
add_numbers(3, 5)

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n=== Practice Exercises ===")
print("1. Write a recursive function to find the sum of digits in a number")
print("2. Create a memoization decorator to speed up Fibonacci")
print("3. Write a function that returns a function to check if a number is divisible by n")
print("4. Create a decorator that times how long a function takes to execute")
