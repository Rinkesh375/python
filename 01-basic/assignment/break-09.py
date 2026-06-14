# ==========================================
# for-else and break Notes
# ==========================================

# In Python, an else block can be attached to a for loop.
#
# The else block runs ONLY when the loop completes normally.
#
# If a break statement is executed inside the loop,
# the else block is skipped.

charCount = {}

# Count occurrences of each character
for ch in string:
    charCount[ch] = charCount.get(ch, 0) + 1

# Find the first character that appears only once
for ch in string:
    if charCount[ch] == 1:
        print("First non-repeated character =", ch)

        # Stop the loop immediately when a match is found
        break

# Runs only if the loop finishes without break
else:
    print("No non-repeated character found.")

# ==========================================
# Example 1
# ==========================================
#
# Input:
# swiss
#
# Counts:
# {
#     's': 3,
#     'w': 1,
#     'i': 1
# }
#
# Execution:
# s -> count = 3
# w -> count = 1 -> Found
# break executes
#
# Output:
# First non-repeated character = w
#
# else block is NOT executed.


# ==========================================
# Example 2
# ==========================================
#
# Input:
# aabbcc
#
# Counts:
# {
#     'a': 2,
#     'b': 2,
#     'c': 2
# }
#
# No character has count == 1
# break never executes
#
# Output:
# No non-repeated character found.
#
# else block IS executed.


# ==========================================
# Memory Trick
# ==========================================
#
# for item in collection:
#     if condition:
#         break
# else:
#     # Runs only if NO break occurred
#
#
# Loop ended with break?
#     Yes -> Skip else
#     No  -> Run else