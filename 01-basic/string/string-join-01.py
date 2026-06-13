# ==========================================
# join() Method in Python
# ==========================================

# The join() method is used to combine all
# elements of an iterable (list, tuple, etc.)
# into a single string.

# Syntax:
# separator.join(iterable)

# ------------------------------------------
# Example
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun", "Ajay", "Vijay"]

print("".join(array))
print(" ".join(array))
print(", ".join(array))
print("|".join(array))

# Output:
# RinkeshKaranArjunAjayVijay
# Rinkesh Karan Arjun Ajay Vijay
# Rinkesh, Karan, Arjun, Ajay, Vijay
# Rinkesh|Karan|Arjun|Ajay|Vijay

# ------------------------------------------
# Explanation
# ------------------------------------------

# "".join(array)
# Joins all elements without any separator.

# " ".join(array)
# Inserts a space between elements.

# ", ".join(array)
# Inserts a comma and space between elements.

# "|".join(array)
# Inserts a pipe (|) between elements.

# ------------------------------------------
# Real-World Example 1: Create CSV Data
# ------------------------------------------

cities = ["Delhi", "Mumbai", "Pune"]

result = ",".join(cities)

print(result)

# Output:
# Delhi,Mumbai,Pune

# ------------------------------------------
# Real-World Example 2: Create a Sentence
# ------------------------------------------

words = ["Python", "is", "easy", "to", "learn"]

print(" ".join(words))

# Output:
# Python is easy to learn

# ------------------------------------------
# Important Note
# ------------------------------------------

# join() only works with strings.

# Wrong Example:
# numbers = [1, 2, 3]
# print(",".join(numbers))
#
# Error:
# TypeError: expected str instance, int found

# Correct Example:

numbers = [1, 2, 3]

print(",".join(map(str, numbers)))

# Output:
# 1,2,3

# ------------------------------------------
# Interview Notes
# ------------------------------------------

# 1. join() combines multiple strings into
#    a single string.

# 2. The separator is written before join().

# 3. More efficient than repeatedly using
#    the + operator for string concatenation.

# 4. Works only with string elements.

# Common Separators:
# ""   -> No separator
# " "  -> Space
# ","  -> Comma
# "|"  -> Pipe
# "-"  -> Hyphen

# ------------------------------------------
# Quick Revision
# ------------------------------------------

arr = ["A", "B", "C"]

print("".join(arr))   # ABC
print(" ".join(arr))  # A B C
print(",".join(arr))  # A,B,C
print("|".join(arr))  # A|B|C





for name in array:
    print(name)






string = "My name is \"Rinkesh\"."

print(string)


print("------------------------------------------------------------------------------------------")


# ==========================================
# Escape Characters in Python
# ==========================================

# Escape characters are used when we want to
# include special characters inside a string.

# \" is used to include double quotes (")
# inside a string enclosed by double quotes.

# ------------------------------------------
# Example
# ------------------------------------------

string = "My name is \"Rinkesh\"."

print(string)

# Output:
# My name is "Rinkesh".

# ------------------------------------------
# Explanation
# ------------------------------------------

# Normally, Python treats double quotes (")
# as the beginning and end of a string.

# Example (Invalid):

# string = "My name is "Rinkesh"."
#
# This will cause a SyntaxError because
# Python thinks the string ends before Rinkesh.

# To include double quotes inside a string,
# use the escape character (\).

# Correct:

# string = "My name is \"Rinkesh\"."

# ------------------------------------------
# Common Escape Characters
# ------------------------------------------

# \"  -> Double Quote
# \'  -> Single Quote
# \\  -> Backslash
# \n  -> New Line
# \t  -> Tab Space

# ------------------------------------------
# More Examples
# ------------------------------------------

print("He said, \"Hello!\"")

# Output:
# He said, "Hello!"

print('It\'s a beautiful day.')

# Output:
# It's a beautiful day.

print("C:\\Users\\Rinkesh")

# Output:
# C:\Users\Rinkesh

print("Hello\nWorld")

# Output:
# Hello
# World

print("Name\tAge")

# Output:
# Name    Age

# ------------------------------------------
# Interview Notes
# ------------------------------------------

# 1. Escape characters start with a backslash (\).

# 2. They allow special characters to be used
#    inside strings.

# 3. \" is used to print double quotes inside
#    a string.

# 4. \n creates a new line.

# 5. \t creates a tab space.

# 6. \\ prints a single backslash.

# ------------------------------------------
# Quick Revision
# ------------------------------------------

print("\"Python\"")    # "Python"
print("A\nB")          # A (new line) B
print("A\tB")          # A    B
print("\\")            # \




print("------------------------------------------------------------------------------------------")




# ==========================================
# Raw String in Python
# ==========================================

# A raw string is created by placing 'r'
# before the string.

# Raw strings treat backslashes (\) as
# normal characters and do not interpret
# them as escape characters.

# ------------------------------------------
# Example
# ------------------------------------------

string = r"c:\users\rinkesh\Desktop"

print(string)

# Output:
# c:\users\rinkesh\Desktop

# ------------------------------------------
# Why Use Raw Strings?
# ------------------------------------------

# Normally, backslashes are used for
# escape sequences in Python.

# Examples:
# \n -> New Line
# \t -> Tab
# \\ -> Backslash

# When working with file paths, writing
# multiple backslashes can become messy.

# Without Raw String:

path = "c:\\users\\rinkesh\\Desktop"

print(path)

# Output:
# c:\users\rinkesh\Desktop

# With Raw String:

path = r"c:\users\rinkesh\Desktop"

print(path)

# Output:
# c:\users\rinkesh\Desktop

# ------------------------------------------
# Explanation
# ------------------------------------------

# r"..." tells Python:
# "Treat everything inside the string
# literally."

# Therefore:
# \n is not converted to a new line.
# \t is not converted to a tab.
# They remain as normal text.

# ------------------------------------------
# Example
# ------------------------------------------

print(r"Hello\nWorld")

# Output:
# Hello\nWorld

# Instead of:
#
# Hello
# World

# ------------------------------------------
# Interview Notes
# ------------------------------------------

# 1. Prefix 'r' creates a raw string.
#
# 2. Raw strings ignore escape sequences.
#
# 3. Commonly used for:
#    - File paths
#    - Regular Expressions (Regex)
#    - Windows directory locations
#
# 4. Makes strings containing backslashes
#    easier to read and write.

# ------------------------------------------
# Quick Revision
# ------------------------------------------

print(r"C:\Users\Admin")
print(r"Hello\nPython")
print(r"Folder\Files\Data")

# Output:
# C:\Users\Admin
# Hello\nPython
# Folder\Files\Data



print("------------------------------------------------------------------------------------------")

string = "Rinkesh"

print("r" in string)


print("R" in string)


print("s" in string)


print("a" in string)