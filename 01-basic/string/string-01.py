# ==========================================
# STRING INDEXING & SLICING NOTES
# ==========================================

name = "Rinkesh Kumar"

# Index Positions
#
# Character: R i n k e s h   K u m a r
# Index:     0 1 2 3 4 5 6 7 8 9 10 11 12
#
# Negative Index:
# Character: R i n k e s h   K u m a r
# Index:    -13.................      -1


# ==========================================
# STRING INDEXING
# ==========================================

# Access a single character using its index

firstCharacter = name[0]
print(firstCharacter)

# Output:
# R


# ==========================================
# STRING SLICING
# ==========================================

# Syntax:
# string[start:end]

# start = where to begin
# end = where to stop (NOT included)

print(name[0:7])

# Output:
# Rinkesh

# Python takes characters from index 0 to 6
# Index 7 is NOT included


# ==========================================
# NEGATIVE INDEXING
# ==========================================

print(name[-1])

# Output:
# r

# -1 means last character
# -2 means second last character
# -3 means third last character


# ==========================================
# OMITTING THE END INDEX
# ==========================================

print(name[4:])

# Output:
# esh Kumar

# Start at index 4
# Continue until the end


# ==========================================
# COPY ENTIRE STRING
# ==========================================

print(name[:])

# Output:
# Rinkesh Kumar

# No start + no end
# Returns the entire string


# ==========================================
# OMITTING THE START INDEX
# ==========================================

print(name[:6])

# Output:
# Rinkes

# Start from beginning (index 0)
# Stop before index 6


# ==========================================
# ADVANCED SLICING (STEP)
# ==========================================

# Syntax:
# string[start:end:step]

# start = where to begin
# end = where to stop (NOT included)
# step = how many positions to jump

print(name[0:8:3])

# Output:
# Rke


# Detailed Breakdown:
#
# Character: R i n k e s h
# Index:     0 1 2 3 4 5 6
#
# Start at index 0 -> R
#
# Jump 3 positions:
# 0 + 3 = 3 -> k
#
# Jump 3 more positions:
# 3 + 3 = 6 -> e
#
# Jump 3 more positions:
# 6 + 3 = 9 (outside range)
#
# Stop
#
# Result:
# Rke


# ==========================================
# COMMON STEP EXAMPLES
# ==========================================

name = "Rinkesh"

print(name[0:7:1])

# Output:
# Rinkesh
#
# Step 1 = Take every character


print(name[0:7:2])

# Output:
# Rneh
#
# Take every 2nd character
#
# Index:
# 0 -> R
# 2 -> n
# 4 -> e
# 6 -> h


print(name[0:7:3])

# Output:
# Rke
#
# Take every 3rd character
#
# Index:
# 0 -> R
# 3 -> k
# 6 -> e


# ==========================================
# REVERSE A STRING
# ==========================================

print(name[::-1])

# Output:
# ramuK hsekniR
#
# Step = -1
# Move backwards one character at a time


# ==========================================
# IMPORTANT RULES
# ==========================================

# string[start:end]
#
# Start is INCLUDED
# End is EXCLUDED

# Example:
# name[0:4]
#
# Takes:
# 0,1,2,3
#
# Does NOT take:
# 4


# ==========================================
# MEMORY TRICK
# ==========================================

# string[start:end:step]
#
# start = Where to start
# end   = Where to stop (not included)
# step  = How many positions to jump
#
# Positive step -> Move forward
# Negative step -> Move backward
# Step = 0 -> ERROR



print("------------------------------------------------------------------")

# ==========================================
# PYTHON STRING METHODS NOTES
# ==========================================

# String used in examples

name = "rajkUMAR"


# ==========================================
# capitalize()
# ==========================================

print("rajkUMAR".capitalize())

# Output:
# Rajkumar

# What it does:
# Converts the first character to uppercase
# Converts all remaining characters to lowercase

# Example:
# "hello world" -> "Hello world"
# "PYTHON" -> "Python"


# ==========================================
# lower()
# ==========================================

print("rajkUMAR".lower())

# Output:
# rajkumar

# What it does:
# Converts all characters to lowercase

# Example:
# "HELLO" -> "hello"
# "PyThOn" -> "python"


# ==========================================
# upper()
# ==========================================

print("rajkUMAR".upper())

# Output:
# RAJKUMAR

# What it does:
# Converts all characters to uppercase

# Example:
# "hello" -> "HELLO"
# "Python" -> "PYTHON"


# ==========================================
# strip()
# ==========================================

print("           Hello World                   ".strip())

# Output:
# Hello World

# What it does:
# Removes whitespace from BOTH sides
# (beginning and end of the string)

# Before:
# "     Hello World     "

# After:
# "Hello World"

# Note:
# strip() DOES NOT remove spaces between words

# Example:
# "   Hello   World   "
#
# After strip():
# "Hello   World"


# ==========================================
# lstrip()
# ==========================================

print("     Hello World     ".lstrip())

# Output:
# Hello World

# Removes spaces from LEFT side only


# ==========================================
# rstrip()
# ==========================================

print("     Hello World     ".rstrip())

# Output:
#      Hello World

# Removes spaces from RIGHT side only


# ==========================================
# MEMORY TRICK
# ==========================================

# capitalize() -> First letter uppercase, rest lowercase
#
# lower()      -> Everything lowercase
#
# upper()      -> Everything uppercase
#
# strip()      -> Remove spaces from both sides
#
# lstrip()     -> Remove spaces from left side
#
# rstrip()     -> Remove spaces from right side


# ==========================================
# INTERVIEW NOTES
# ==========================================

# Strings are immutable in Python.
#
# String methods DO NOT modify the original string.
# They return a NEW string.

name = "rajkUMAR"

print(name.upper())  # RAJKUMAR
print(name)          # rajkUMAR

# Original string remains unchanged.




print("###########################################################")


# ==========================================
# PYTHON STRING METHODS NOTES
# ==========================================


# ==========================================
# replace()
# ==========================================

print("Rinkesh Kumar".replace("Kumar", "Jha"))

# Output:
# Rinkesh Jha

# What it does:
# Replaces all occurrences of a substring
# with a new substring.

# Syntax:
# string.replace(old_value, new_value)

# Example:
# "Hello World".replace("World", "Python")
#
# Output:
# Hello Python

# Note:
# Original string is NOT modified.
# A new string is returned.


# ==========================================
# split()
# ==========================================

print("Nitish, Rinkesh, Pulkit, Abhishek".split(", "))

# Output:
# ['Nitish', 'Rinkesh', 'Pulkit', 'Abhishek']

# What it does:
# Splits a string into a list based on a separator.

# Syntax:
# string.split(separator)

# Example:
# "apple,banana,mango".split(",")
#
# Output:
# ['apple', 'banana', 'mango']

# Common use case:
# Converting CSV-like text into a list.


# ==========================================
# find()
# ==========================================

print("Nitish, Rinkesh, Pulkit, Abhishek".find("i"))

# Output:
# 1

# What it does:
# Returns the index of the FIRST occurrence
# of the specified value.

# Syntax:
# string.find(value)

# Example:
# "Python".find("t")
#
# Output:
# 2

# Index Positions:
#
# N i t i s h
# 0 1 2 3 4 5
#
# First 'i' found at index 1


# ==========================================
# If value is not found
# ==========================================

print("Python".find("z"))

# Output:
# -1

# -1 means:
# Value not found in the string.


# ==========================================
# MEMORY TRICK
# ==========================================

# replace() -> Replace text
#
# split()   -> Convert string into list
#
# find()    -> Find index of first occurrence


# ==========================================
# INTERVIEW NOTES
# ==========================================

# replace()
# Returns a NEW string with replaced values.

# split()
# Returns a LIST.

# find()
# Returns index if found.
# Returns -1 if not found.

# All string methods return new values.
# They do NOT modify the original string.




print("Nitish, Rinkesh, Pulkit, Abhishek".count("i"))



# ==========================================
# PYTHON STRING FORMATTING - format()
# ==========================================

print("My name is {}. I live in {} currently. It has been {} months"
      .format("Rinkesh", "FBD", 4))

# Output:
# My name is Rinkesh. I live in FBD currently. It has been 4 months


# ==========================================
# What does format() do?
# ==========================================

# format() inserts values into placeholders {}

# Syntax:
# "Text {} Text {}".format(value1, value2)

# Example:

print("Hello {}".format("Rinkesh"))

# Output:
# Hello Rinkesh


# ==========================================
# How it works
# ==========================================

# Placeholder 1 {} -> "Rinkesh"
# Placeholder 2 {} -> "FBD"
# Placeholder 3 {} -> 4

print("My name is {}. I live in {} currently. It has been {} months"
      .format("Rinkesh", "FBD", 4))

# Result:
# My name is Rinkesh. I live in FBD currently. It has been 4 months


# ==========================================
# Multiple Placeholders
# ==========================================

print("{} + {} = {}".format(5, 5, 10))

# Output:
# 5 + 5 = 10


# ==========================================
# Positional Indexing
# ==========================================

print("My name is {0}. I live in {1}".format("Rinkesh", "FBD"))

# Output:
# My name is Rinkesh. I live in FBD

# {0} -> First value
# {1} -> Second value


# Reusing the same value

print("{0} loves Python. {0} is learning fast.".format("Rinkesh"))

# Output:
# Rinkesh loves Python. Rinkesh is learning fast.


# ==========================================
# Named Placeholders
# ==========================================

print("My name is {name}. I live in {city}"
      .format(name="Rinkesh", city="FBD"))

# Output:
# My name is Rinkesh. I live in FBD


# ==========================================
# Modern Alternative (f-strings)
# ==========================================

name = "Rinkesh"
city = "FBD"
months = 4

print(f"My name is {name}. I live in {city}. It has been {months} months")

# Output:
# My name is Rinkesh. I live in FBD. It has been 4 months

# f-strings are preferred in modern Python (3.6+)


# ==========================================
# MEMORY TRICK
# ==========================================

# {}       -> Placeholder
# format() -> Fill the placeholders with values

# Example:
# "Hello {}".format("Rinkesh")
#          ↓
# "Hello Rinkesh"


# ==========================================
# INTERVIEW NOTES
# ==========================================

# format() is used for string formatting.
#
# {} are placeholders.
#
# Values are inserted in the same order as provided.
#
# Modern Python prefers f-strings because they are
# shorter, faster, and easier to read.



array = ["Rinkesh", "Karan","Arjun", "Ajay", "Vijay"]


print("".join(array))

print(" ".join(array))


print(", ".join(array))


print("|".join(array))


