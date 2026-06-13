# ==========================================
# List Indexing and Slicing in Python
# ==========================================

array = ["Rinkesh", "Karan", "Arjun", "Ajay", "Vijay"]

print(array[-1])          # Last element
print(array[len(array)-1]) # Last element using length

print(array[0:])          # Entire list
print(array[0:4])         # Elements from index 0 to 3

array[0] = "Rinkesh Kumar" # Update element

print(array)

# Output:
# Vijay
# Vijay
# ['Rinkesh', 'Karan', 'Arjun', 'Ajay', 'Vijay']
# ['Rinkesh', 'Karan', 'Arjun', 'Ajay']
# ['Rinkesh Kumar', 'Karan', 'Arjun', 'Ajay', 'Vijay']

# Notes:
# array[-1] -> Last element
# len(array)-1 -> Last index
# array[0:] -> Complete list
# array[0:4] -> Index 0 to 3
# array[index] = value -> Update element



array[0:1] = "Rinkesh"

print(array)



print("----------------------------------------------------------------------------------------------")


# ==========================================
# Slice Assignment in Python Lists
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

array[0:1] = "Rinkesh"

print(array)

# Output:
# ['R', 'i', 'n', 'k', 'e', 's', 'h',
#  'Karan', 'Arjun']

# ------------------------------------------
# Why Did This Happen?
# ------------------------------------------

# array[0] refers to a single position.
# array[0:1] refers to a slice (part of the list).

# When assigning to a slice, Python expects
# multiple items.

# A string is iterable, meaning Python can
# loop through each character.

# Therefore:

# array[0:1] = "Rinkesh"

# is treated like:

# array[0:1] = ['R', 'i', 'n', 'k', 'e', 's', 'h']

# So the first element is replaced with
# individual characters.

# ------------------------------------------
# Difference
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

array[0] = "Rinkesh Kumar"

print(array)

# Output:
# ['Rinkesh Kumar', 'Karan', 'Arjun']

# Here only one position is replaced.

# ------------------------------------------
# Correct Way to Replace Slice with One Item
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

array[0:1] = ["Rinkesh Kumar"]



print(array)

# Output:
# ['Rinkesh Kumar', 'Karan', 'Arjun']

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# array[0] = value
# Replace one element.

# array[0:1] = value
# Replace a slice.

# Strings are iterable.
# Python treats "Rinkesh" as:
# 'R', 'i', 'n', 'k', 'e', 's', 'h'

# Use ["Rinkesh"] if you want one item.
# Use "Rinkesh" if you want characters.+



array[0:3] = ["Nitish","Neeraj","Raju"]
print(array)



array[0:0] = ["abc","def","ghi","jkl"]


print(array)


array[0:4] = []

print(array)



print("----------------------------------------------------------------------------------------------")


# ==========================================
# Insert and Delete Using Slice Assignment
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

array[0:0] = ["abc", "def", "ghi", "jkl"]

print(array)

# Output:
# ['abc', 'def', 'ghi', 'jkl','Rinkesh', 'Karan', 'Arjun']

# ------------------------------------------
# Insert Elements
# ------------------------------------------

# array[0:0] means:
# Start at index 0 and end at index 0.
# No elements are selected.

# Since nothing is selected, Python inserts
# the new values at index 0.

# ------------------------------------------
# Delete Elements
# ------------------------------------------

array[0:4] = []

print(array)

# Output:
# ['Rinkesh', 'Karan', 'Arjun']

# array[0:4] selects:
# ['abc', 'def', 'ghi', 'jkl']

# Assigning an empty list [] removes
# all selected elements.

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# array[start:end] = [values]
# Replace selected elements.

# array[0:0] = [values]
# Insert elements at index 0.

# array[0:4] = []
# Delete elements from index 0 to 3.

# [] on the right side means:
# "Replace with nothing" (delete).





array = ["Rinkesh", "Karan", "Arjun"]


for name in array:
    print(name,end="$")



print("-----------------------------------------------------------------------")

# ==========================================
# for Loop in Python List
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

for name in array:
    print(name, end="$")

# Output:
# Rinkesh$Karan$Arjun$

# ------------------------------------------
# Explanation
# ------------------------------------------

# The for loop visits each element
# of the list one by one.

# Iteration 1:
# name = "Rinkesh"

# Iteration 2:
# name = "Karan"

# Iteration 3:
# name = "Arjun"

# ------------------------------------------
# end Parameter
# ------------------------------------------

# By default, print() ends with a new line.

# print("Hello")
# print("World")

# Output:
# Hello
# World

# Using end="$"

# print("Hello", end="$")
# print("World", end="$")

# Output:
# Hello$World$

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# for item in list:
#     Runs once for each element.

# name is a temporary variable.

# end="$" prints $ after each value
# instead of moving to a new line.


print("-----------------------------------------------------------------------")

array = ["Rinkesh", "Karan", "Arjun"]


if "Rinkesh" in array:
    print("Rinkesh is available in array")
else:
    array.append("Rinkesh")
    print(array)




if "Nitish" in array:
    print("Nitish is available in array")
else:
    array.append("Nitish")
    print(array)



print(array.pop())
print(array)




print(array)

print(array.remove("Rinkesh"))

print(array)



print("==============================================================================")

# ==========================================
# pop() and remove() in Python Lists
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

print(array.pop())

# Output:
# Arjun

print(array)

# Output:
# ['Rinkesh', 'Karan']

# ------------------------------------------
# pop()
# ------------------------------------------

# pop() removes and returns the last element.

# Syntax:
# array.pop()

# You can also remove by index:
# array.pop(0)

# ------------------------------------------
# remove()
# ------------------------------------------

array.remove("Rinkesh")

print(array)

# Output:
# ['Karan']

# remove(value) removes the first matching value.

# Syntax:
# array.remove("value")

# ------------------------------------------
# What if Value Does Not Exist?
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

# array.remove("Abhishek")

# Error:
# ValueError: list.remove(x): x not in list

# Safe Way:

if "Abhishek" in array:
    array.remove("Abhishek")
else:
    print("Abhishek not found")

# Output:
# Abhishek not found

# ------------------------------------------
# Important Note
# ------------------------------------------

# print(array.remove("Rinkesh"))

# Output:
# None

# Why?

# remove() modifies the list directly and
# does not return anything.

# Therefore it returns None.

# Correct:

array.remove("Rinkesh")
print(array)

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# pop()           -> Removes last element
# pop(index)      -> Removes element at index
# remove(value)   -> Removes matching value
# remove()        -> Returns None
# remove(value)   -> Raises ValueError if value is not found
# Use "if value in list" before remove()



# ==========================================
# insert() Method in Python List
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

array.insert(2, "Rajkumar")

print(array)

# Output:
# ['Rinkesh', 'Karan', 'Rajkumar', 'Arjun']

# ------------------------------------------
# insert(index, value)
# ------------------------------------------

# insert() adds an element at a specific index.

# Syntax:
# array.insert(index, value)

# Example:
# array.insert(2, "Rajkumar")

# Inserts "Rajkumar" at index 2.

# Existing elements are shifted to the right.

# ------------------------------------------
# Invalid Syntax
# ------------------------------------------

# array.insert("Dinesh")

# Error:
# TypeError: insert expected 2 arguments, got 1

# insert() requires:
# 1. Index
# 2. Value

# Correct:

# array.insert(0, "Dinesh")

# ------------------------------------------
# More Examples
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

array.insert(0, "Dinesh")

print(array)

# Output:
# ['Dinesh', 'Rinkesh', 'Karan', 'Arjun']

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# insert(index, value)
# Adds an element at a specific position.

# Existing elements move right.

# insert() modifies the original list.

# insert() requires exactly 2 arguments:
# index and value.


print("=================================================================================================")

# ==========================================
# copy() Method in Python List
# ==========================================

array = ["Rinkesh", "Karan", "Arjun"]

array2 = array.copy()

print(array)
print(array2)

# Output:
# ['Rinkesh', 'Karan', 'Arjun']
# ['Rinkesh', 'Karan', 'Arjun']

# ------------------------------------------
# What does copy() do?
# ------------------------------------------

# copy() creates a new list with the same
# elements as the original list.

# array and array2 are different objects
# in memory.

# Example:

array2[0] = "Rajkumar"

print(array)
print(array2)

# Output:
# ['Rinkesh', 'Karan', 'Arjun']
# ['Rajkumar', 'Karan', 'Arjun']

# Changing array2 does NOT affect array.

# ------------------------------------------
# Memory Check
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

array2 = array.copy()

print(id(array))
print(id(array2))

# Output:
# Different memory addresses

# ------------------------------------------
# Difference
# ------------------------------------------

array = ["Rinkesh", "Karan", "Arjun"]

array2 = array

# Both variables point to the SAME list.

array2[0] = "Rajkumar"

print(array)

# Output:
# ['Rajkumar', 'Karan', 'Arjun']

# array is also changed because both
# variables refer to the same object.

# ------------------------------------------
# Quick Notes
# ------------------------------------------

# array2 = array
# Same list, same memory location.

# array2 = array.copy()
# New list, different memory location.

# copy() creates a shallow copy.

# Changes to array2 do not affect array
# for normal list elements.