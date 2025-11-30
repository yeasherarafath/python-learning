"""
Practice Exercises - Basic Problems
===================================
This module contains basic practice problems with solutions.
Try to solve each problem before looking at the solution!
"""

# ============================================================================
# PROBLEM 1: Calculate Average
# ============================================================================
print("=== Problem 1: Calculate Average ===")
print("Write a function that calculates the average of a list of numbers")


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numbers
    
    Returns:
        The average as a float, or 0 if the list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Test
test_numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {test_numbers}")
print(f"Average: {calculate_average(test_numbers)}")
print(f"Empty list average: {calculate_average([])}")


# ============================================================================
# PROBLEM 2: Check Prime Number
# ============================================================================
print("\n=== Problem 2: Check Prime Number ===")
print("Write a function that checks if a number is prime")


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check
    
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Test
test_nums = [1, 2, 3, 4, 5, 17, 20, 23, 100]
print("Prime number check:")
for num in test_nums:
    print(f"  {num}: {'Prime' if is_prime(num) else 'Not Prime'}")


# ============================================================================
# PROBLEM 3: Reverse a String
# ============================================================================
print("\n=== Problem 3: Reverse a String ===")
print("Write a function that reverses a string without using slicing")


def reverse_string(s):
    """
    Reverse a string without using slicing.
    
    Args:
        s: String to reverse
    
    Returns:
        Reversed string
    """
    result = ""
    for char in s:
        result = char + result
    return result


# Alternative using list
def reverse_string_alt(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


# Test
test_string = "Hello, World!"
print(f"Original: {test_string}")
print(f"Reversed: {reverse_string(test_string)}")
print(f"Reversed (alt): {reverse_string_alt(test_string)}")


# ============================================================================
# PROBLEM 4: Count Vowels
# ============================================================================
print("\n=== Problem 4: Count Vowels ===")
print("Write a function that counts the number of vowels in a string")


def count_vowels(s):
    """
    Count vowels in a string.
    
    Args:
        s: String to check
    
    Returns:
        Number of vowels (a, e, i, o, u)
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# Alternative using comprehension
def count_vowels_alt(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


# Test
test_text = "Python Programming is Amazing!"
print(f"Text: {test_text}")
print(f"Vowel count: {count_vowels(test_text)}")


# ============================================================================
# PROBLEM 5: Find Factorial
# ============================================================================
print("\n=== Problem 5: Find Factorial ===")
print("Write functions to find factorial using iteration and recursion")


def factorial_iterative(n):
    """Calculate factorial using iteration."""
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# Test
for num in range(6):
    iter_result = factorial_iterative(num)
    rec_result = factorial_recursive(num)
    print(f"  {num}! = {iter_result} (iterative) = {rec_result} (recursive)")


# ============================================================================
# PROBLEM 6: Fibonacci Sequence
# ============================================================================
print("\n=== Problem 6: Fibonacci Sequence ===")
print("Write a function that generates the first n Fibonacci numbers")


def fibonacci_sequence(n):
    """
    Generate first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
    
    Returns:
        List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# Test
print(f"First 10 Fibonacci numbers: {fibonacci_sequence(10)}")
print(f"First 15 Fibonacci numbers: {fibonacci_sequence(15)}")


# ============================================================================
# PROBLEM 7: Check Palindrome
# ============================================================================
print("\n=== Problem 7: Check Palindrome ===")
print("Write a function that checks if a string is a palindrome")


def is_palindrome(s):
    """
    Check if a string is a palindrome (ignoring case and spaces).
    
    Args:
        s: String to check
    
    Returns:
        True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = "".join(s.lower().split())
    return cleaned == cleaned[::-1]


# Test
test_strings = ["radar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw"]
print("Palindrome check:")
for text in test_strings:
    result = "Yes" if is_palindrome(text) else "No"
    print(f"  '{text}': {result}")


# ============================================================================
# PROBLEM 8: FizzBuzz
# ============================================================================
print("\n=== Problem 8: FizzBuzz ===")
print("Print numbers 1-20: 'Fizz' for multiples of 3, 'Buzz' for 5, 'FizzBuzz' for both")


def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    Returns list of strings: number, 'Fizz', 'Buzz', or 'FizzBuzz'
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# Test
print("FizzBuzz 1-20:")
fb_result = fizzbuzz(20)
for i in range(0, 20, 5):
    print(f"  {', '.join(fb_result[i:i+5])}")


# ============================================================================
# PROBLEM 9: Remove Duplicates
# ============================================================================
print("\n=== Problem 9: Remove Duplicates ===")
print("Remove duplicates from a list while preserving order")


def remove_duplicates(lst):
    """
    Remove duplicates while preserving order.
    
    Args:
        lst: List with possible duplicates
    
    Returns:
        List with duplicates removed, order preserved
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Test
test_list = [1, 2, 2, 3, 4, 3, 5, 1, 6, 4]
print(f"Original: {test_list}")
print(f"Without duplicates: {remove_duplicates(test_list)}")


# ============================================================================
# PROBLEM 10: Find Second Largest
# ============================================================================
print("\n=== Problem 10: Find Second Largest ===")
print("Find the second largest number in a list")


def second_largest(numbers):
    """
    Find the second largest number in a list.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Second largest number, or None if not enough unique numbers
    """
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]


# Alternative without sorting
def second_largest_alt(numbers):
    if len(numbers) < 2:
        return None
    
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None


# Test
test_nums = [5, 2, 8, 1, 9, 3, 9, 8]
print(f"Numbers: {test_nums}")
print(f"Second largest: {second_largest(test_nums)}")
print(f"Second largest (alt): {second_largest_alt(test_nums)}")
