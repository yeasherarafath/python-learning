"""
Practice Exercises - Intermediate Problems
==========================================
This module contains intermediate practice problems with solutions.
Try to solve each problem before looking at the solution!
"""

import string

# ============================================================================
# PROBLEM 1: Two Sum
# ============================================================================
print("=== Problem 1: Two Sum ===")
print("Find two numbers in a list that add up to a target sum")


def two_sum(numbers, target):
    """
    Find indices of two numbers that add up to target.
    
    Args:
        numbers: List of integers
        target: Target sum
    
    Returns:
        Tuple of indices, or None if not found
    """
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


# Test
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Numbers: {nums}, Target: {target}")
print(f"Indices: {result}")  # (0, 1) because 2 + 7 = 9


# ============================================================================
# PROBLEM 2: Valid Anagram
# ============================================================================
print("\n=== Problem 2: Valid Anagram ===")
print("Check if two strings are anagrams of each other")


def is_anagram(s1, s2):
    """
    Check if two strings are anagrams (same characters, different order).
    
    Args:
        s1: First string
        s2: Second string
    
    Returns:
        True if anagrams, False otherwise
    """
    # Remove spaces and convert to lowercase
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    if len(s1_clean) != len(s2_clean):
        return False
    
    # Count characters
    char_count = {}
    for char in s1_clean:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s2_clean:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True


# Test
pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("Dormitory", "Dirty Room"),
    ("anagram", "nagaram")
]
print("Anagram check:")
for s1, s2 in pairs:
    result = "Yes" if is_anagram(s1, s2) else "No"
    print(f"  '{s1}' and '{s2}': {result}")


# ============================================================================
# PROBLEM 3: Merge Sorted Lists
# ============================================================================
print("\n=== Problem 3: Merge Sorted Lists ===")
print("Merge two sorted lists into one sorted list")


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1: First sorted list
        list2: Second sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result


# Test
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8, 10]
print(f"List 1: {l1}")
print(f"List 2: {l2}")
print(f"Merged: {merge_sorted_lists(l1, l2)}")


# ============================================================================
# PROBLEM 4: Find Missing Number
# ============================================================================
print("\n=== Problem 4: Find Missing Number ===")
print("Find the missing number in a list containing n-1 integers from 1 to n")


def find_missing_number(numbers, n):
    """
    Find the missing number from 1 to n.
    
    Args:
        numbers: List containing n-1 integers from 1 to n
        n: The upper bound
    
    Returns:
        The missing number
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


# Test
n = 10
nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]  # 5 is missing
print(f"Numbers (1 to {n}): {nums}")
print(f"Missing number: {find_missing_number(nums, n)}")


# ============================================================================
# PROBLEM 5: Group Anagrams
# ============================================================================
print("\n=== Problem 5: Group Anagrams ===")
print("Group words that are anagrams of each other")


def group_anagrams(words):
    """
    Group anagrams together.
    
    Args:
        words: List of strings
    
    Returns:
        List of groups (each group is a list of anagrams)
    """
    groups = {}
    for word in words:
        # Sort characters to create key
        key = "".join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Words: {words}")
print(f"Grouped anagrams: {group_anagrams(words)}")


# ============================================================================
# PROBLEM 6: Rotate List
# ============================================================================
print("\n=== Problem 6: Rotate List ===")
print("Rotate a list by k positions to the right")


def rotate_list(lst, k):
    """
    Rotate list k positions to the right.
    
    Args:
        lst: List to rotate
        k: Number of positions
    
    Returns:
        Rotated list
    """
    if not lst:
        return lst
    
    k = k % len(lst)  # Handle k larger than list length
    return lst[-k:] + lst[:-k]


# Test
original = [1, 2, 3, 4, 5]
for k in [1, 2, 3]:
    print(f"Original: {original}, Rotate by {k}: {rotate_list(original, k)}")


# ============================================================================
# PROBLEM 7: Valid Parentheses
# ============================================================================
print("\n=== Problem 7: Valid Parentheses ===")
print("Check if a string has valid matching parentheses")


def is_valid_parentheses(s):
    """
    Check if parentheses are balanced.
    
    Args:
        s: String containing brackets
    
    Returns:
        True if valid, False otherwise
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        elif char in "({[":
            stack.append(char)
    
    return len(stack) == 0


# Test
test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "((()))"]
print("Parentheses validation:")
for case in test_cases:
    result = "Valid" if is_valid_parentheses(case) else "Invalid"
    print(f"  '{case}': {result}")


# ============================================================================
# PROBLEM 8: Longest Common Prefix
# ============================================================================
print("\n=== Problem 8: Longest Common Prefix ===")
print("Find the longest common prefix among a list of strings")


def longest_common_prefix(strings):
    """
    Find longest common prefix.
    
    Args:
        strings: List of strings
    
    Returns:
        Longest common prefix string
    """
    if not strings:
        return ""
    
    # Start with the first string
    prefix = strings[0]
    
    for s in strings[1:]:
        # Reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


# Test
words1 = ["flower", "flow", "flight"]
words2 = ["dog", "racecar", "car"]
print(f"Words: {words1}")
print(f"Longest common prefix: '{longest_common_prefix(words1)}'")
print(f"Words: {words2}")
print(f"Longest common prefix: '{longest_common_prefix(words2)}'")


# ============================================================================
# PROBLEM 9: Matrix Transpose
# ============================================================================
print("\n=== Problem 9: Matrix Transpose ===")
print("Transpose a 2D matrix (swap rows and columns)")


def transpose_matrix(matrix):
    """
    Transpose a matrix.
    
    Args:
        matrix: 2D list (list of lists)
    
    Returns:
        Transposed matrix
    """
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create transposed matrix
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed


# Using comprehension
def transpose_matrix_comp(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))] if matrix else []


# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix:")
for row in matrix:
    print(f"  {row}")

transposed = transpose_matrix(matrix)
print("\nTransposed matrix:")
for row in transposed:
    print(f"  {row}")


# ============================================================================
# PROBLEM 10: Word Frequency Counter
# ============================================================================
print("\n=== Problem 10: Word Frequency Counter ===")
print("Count the frequency of each word in a text")


def word_frequency(text):
    """
    Count word frequency in text.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with word counts
    """
    # Remove punctuation and convert to lowercase
    clean_text = text.lower()
    for char in string.punctuation:
        clean_text = clean_text.replace(char, "")
    
    words = clean_text.split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


def top_n_words(text, n=5):
    """Return top n most frequent words."""
    freq = word_frequency(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


# Test
sample_text = """
Python is a great programming language. Python is easy to learn.
Python is used for web development, data science, and more.
I love Python programming!
"""

print(f"Text: {sample_text.strip()}")
print("\nWord frequency:")
for word, count in top_n_words(sample_text, 5):
    print(f"  '{word}': {count}")
