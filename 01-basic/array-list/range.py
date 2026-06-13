# ==========================================
# List Comprehension in Python
# ==========================================

squareNumbers = [x**2 for x in range(20)]

print(squareNumbers)

# Output:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81,
#  100, 121, 144, 169, 196, 225, 256,
#  289, 324, 361]

# ------------------------------------------
# Explanation
# ------------------------------------------

# range(20) generates numbers from 0 to 19.

# x**2 means x raised to the power of 2
# (square of x).

# List comprehension creates a list in
# a single line.

# Syntax:
# [expression for item in iterable]

# ------------------------------------------
# Equivalent for Loop
# ------------------------------------------

squareNumbers = []

for x in range(20):
    squareNumbers.append(x**2)

print(squareNumbers)

# Produces the same output.

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# x**2 -> Square of x

# range(20)
# Generates numbers from 0 to 19

# [x**2 for x in range(20)]
# Creates a list of square numbers

# List comprehension is a shorter and
# cleaner way to create lists.

# ------------------------------------------
# More Examples
# ------------------------------------------

# Create a list of numbers
numbers = [x for x in range(5)]

# Output:
# [0, 1, 2, 3, 4]

# Create a list of cubes
cubes = [x**3 for x in range(5)]

# Output:
# [0, 1, 8, 27, 64]