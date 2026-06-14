# ==========================================
# Dictionary Comprehension and fromkeys()
# ==========================================

# Dictionary containing a list of square numbers.
# Here, the key is "2square" and the value is a list.

object1 = {
    "2square": [x**2 for x in range(1, 5)]
}

# List comprehension result:
# [1, 4, 9, 16]

print(object1)

# Output:
# {'2square': [1, 4, 9, 16]}


# ==========================================
# Dictionary Comprehension
# ==========================================

# Dictionary comprehension creates key-value pairs dynamically.

object2 = {
    x: x**2 for x in range(1, 5)
}

print(object2)

# Output:
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16
# }

# Explanation:
# Key   -> x
# Value -> x**2

# Similar to:

# object2 = {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16
# }


# ==========================================
# dict.fromkeys()
# ==========================================

# Creates a new dictionary using values from an iterable
# as keys and assigns the same default value to each key.

userNames = [
    "Rinkesh",
    "Abhishek",
    "Shubham",
    "Aditya",
    "Kamal"
]

defaultScore = 0

usersScore = dict.fromkeys(userNames, defaultScore)

print(usersScore)

# Output:
# {
#     'Rinkesh': 0,
#     'Abhishek': 0,
#     'Shubham': 0,
#     'Aditya': 0,
#     'Kamal': 0
# }


# ==========================================
# Notes on dict.fromkeys()
# ==========================================
#
# Syntax:
# dict.fromkeys(iterable, value)
#
# iterable:
# Collection of keys (list, tuple, set, etc.)
#
# value:
# Default value assigned to all keys.
#
# Example:
#
# names = ["A", "B", "C"]
#
# result = dict.fromkeys(names, 100)
#
# Output:
# {
#     'A': 100,
#     'B': 100,
#     'C': 100
# }
#
# ==========================================
# Summary
# ==========================================
#
# 1. List Comprehension
#
# [x**2 for x in range(1, 5)]
#
# Creates:
# [1, 4, 9, 16]
#
#
# 2. Dictionary Comprehension
#
# {x: x**2 for x in range(1, 5)}
#
# Creates:
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16
# }
#
#
# 3. dict.fromkeys()
#
# Creates a dictionary from a collection of keys.
#
# dict.fromkeys(["A", "B"], 0)
#
# Output:
# {
#     'A': 0,
#     'B': 0
# }
#
#
# 4. All keys get the same default value.















userNames = [
    "Rinkesh",
    "Abhishek",
    "Shubham",
    "Aditya",
    "Kamal"
]



usersScore = dict.fromkeys(userNames, userNames)

print(usersScore)