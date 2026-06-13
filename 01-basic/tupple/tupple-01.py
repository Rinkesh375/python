# ==========================================
# Python Tuple Notes
# ==========================================

# Tuple: Ordered collection of items.
# Created using parentheses ().

tupple1 = ("Rinkesh", "Abhishek", "Kamal", "Deepak", "Jay")

# Access elements
tupple1[0]      # First element
tupple1[-1]     # Last element
tupple1[0:]     # All elements

# Last element using length
tupple1[len(tupple1) - 1]

# Tuple is IMMUTABLE
# Values cannot be changed after creation.

#tupple1[0] = "Rinkesh Kumar"  # ❌ Error

# Output:
# TypeError: 'tuple' object does not support item assignment

# Summary:
# 1. Tuple uses ()
# 2. Ordered and indexed
# 3. Supports slicing
# 4. Supports negative indexing
# 5. Immutable (cannot add, remove, or update elements)
# 6. Faster than lists for fixed data




print("====================================================================================================================================")


# ==========================================
# Tuple Concatenation (+)
# ==========================================

tupple2 = ("Raj", "Raju", "Rahul", "Modi", "Kejriwal")

# Combine two tuples
allUsersName = tupple1 + tupple2

# Order matters
allUsersName2 = tupple2 + tupple1

print(allUsersName)
print(allUsersName2)

# Output:
# ('Rinkesh', 'Abhishek', ..., 'Kejriwal')
# ('Raj', 'Raju', ..., 'Jay')

# Summary:
# tuple1 + tuple2 -> Creates a new tuple containing elements of both tuples.


print("====================================================================")


# ==========================================
# Membership Operator (in)
# ==========================================

if "Rinkesh" in tupple2:
    print("Rinkesh is there in tupple2")
else:
    print("No Rinkesh")

# Output:
# No Rinkesh

# Summary:
# value in tuple -> Returns True if value exists, otherwise False.


print("====================================================================")


# ==========================================
# count() Method
# ==========================================

tupple3 = (
    "Rinkesh",
    "Modi",
    "LOP Rahul",
    "Modi Ji",
    "Rahul Gandhi"
)

print(tupple3.count("Modi"))
print(tupple3.count("Rahul"))
print(tupple3.count("Rinkesh"))

# Output:
# 1
# 0
# 1

# Explanation:
# "Modi" exists exactly once -> 1
# "Rahul" does not exist exactly -> 0
# ("LOP Rahul" and "Rahul Gandhi" are different strings)
# "Rinkesh" exists once -> 1

# Summary:
# tuple.count(value)
# -> Returns the number of exact matches.
# -> Case-sensitive.
# -> Partial matches are not counted.
#
# Example:
# "Rahul" != "LOP Rahul"
# "Rahul" != "Rahul Gandhi"




print("====================================================================================================================================")



# ==========================================
# Tuple Unpacking
# ==========================================

tupple3 = ("Rinkesh", "Modi", "LOP Rahul", "Modi Ji", "Rahul Gandhi")

# Unpack tuple values into variables
(user1, user2, user3, user4, user5) = tupple3

print(user1, user2, user3, user4, user5)

# Output:
# Rinkesh Modi LOP Rahul Modi Ji Rahul Gandhi


# Number of variables must match
# the number of tuple elements

(user1, user2, user3, user4, user5, user6) = tupple3

# ❌ Error:
# ValueError: not enough values to unpack
# (expected 6, got 5)

# Summary:
# (a, b, c) = tuple
# -> Assigns tuple values to variables
#
# Number of variables == Number of tuple elements
# Otherwise Python raises ValueError



