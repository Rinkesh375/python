# ==========================================
# Python Dictionary Notes
# ==========================================

# A dictionary stores data in key-value pairs.
# Syntax:
# dictionary_name = {
#     "key": value
# }

userInfo = {
    "name": "Rinkesh",
    "city": "FBD",
    "Country": "India",
    "Education": "High School",
    "isMarried": False,
    "working": True,
    "age": 25
}

# Print the entire dictionary
print(userInfo)

# Update an existing value using its key
userInfo["name"] = "Rinkesh Kumar"

# Print updated dictionary
print(userInfo)

# Access a value using square brackets []
# If the key does not exist, Python raises a KeyError
print(userInfo["name"])

# get() method safely retrieves a value from a dictionary
# If the key does not exist, it returns None instead of an error

print(userInfo.get("nam"))     # None (key not found)
print(userInfo.get("name"))    # Rinkesh Kumar
print(userInfo.get("naam"))    # None
print(userInfo.get("names"))   # None
print(userInfo.get("NAME"))    # None

# Dictionary keys are CASE-SENSITIVE
# "name" and "NAME" are treated as different keys

print("====================================================================================================")

# Loop through dictionary keys
# 'key' will contain each dictionary key one by one

for key in userInfo:
    print(key, userInfo[key])

# Output Example:
# name Rinkesh Kumar
# city FBD
# Country India
# ...

print("====================================================================================================")

# items() returns both key and value together as tuples

for key, value in userInfo.items():
    print(key, value)

# Output Example:
# name Rinkesh Kumar
# city FBD
# Country India
# Education High School
# isMarried False
# working True
# age 25

# Summary:
# 1. Dictionary stores data as key-value pairs.
# 2. Values can be strings, numbers, booleans, lists, etc.
# 3. Use dict[key] to access a value.
# 4. Use dict.get(key) to safely access a value.
# 5. Dictionary keys are case-sensitive.
# 6. Use a loop to iterate through keys.
# 7. Use items() to get both keys and values together.
# 8. Existing values can be updated using dict[key] = new_value.




# ==========================================
# Dictionary Length, Key Check, and pop()
# ==========================================

print("====================================================================================================")

# len(dictionary)
# Returns the total number of key-value pairs in the dictionary.
# In this example, it returns the number of entries stored in userInfo.

print(len(userInfo))

# Check whether a key exists in the dictionary.
# The 'in' operator returns True if the key is present,
# otherwise it returns False.

if "name" in userInfo:
    # Access and print the value of the 'name' key.
    print("name:{} key is available".format(userInfo["name"]))
else:
    print("name is not available in userInfo: {}".format(userInfo))

# pop(key)
# Removes the specified key from the dictionary.
# Returns the value associated with that key.

# Example:
# If userInfo contains:
# {"name": "Rinkesh", "city": "FBD"}
#
# userInfo.pop("name")
#
# Returns:
# "Rinkesh"
#
# Dictionary becomes:
# {"city": "FBD"}

print(userInfo.pop("name"))

# Print the dictionary after removing the key.
print(userInfo)

# ==========================================
# Summary
# ==========================================
#
# 1. len(dictionary)
#    - Returns the total number of key-value pairs.
#
# 2. key in dictionary
#    - Checks if a key exists.
#    - Returns True or False.
#
# 3. pop(key)
#    - Removes a key from the dictionary.
#    - Returns the removed value.
#    - Raises KeyError if the key does not exist.
#
# 4. After pop(), the removed key can no longer be accessed.
#
# Example:
# userInfo.pop("name")
# userInfo["name"]  # KeyError
#
# To avoid errors:
# userInfo.pop("name", None)
# This returns None if the key is not found.

print("---------------------------------------------------------------------------------------")

# ==========================================
# Dictionary popitem() Method
# ==========================================

# Print the dictionary before removing any item.
print(userInfo)

# popitem()
# Removes and returns the LAST inserted key-value pair
# from the dictionary as a tuple.

print(userInfo.popitem())

# Print the dictionary after removing the last item.
print(userInfo)

# ==========================================
# Notes
# ==========================================
#
# popitem()
# Syntax:
# dictionary.popitem()
#
# Returns:
# (key, value)
#
# Removes:
# The last inserted key-value pair.
#
# Example:
#
# userInfo = {
#     "name": "Rinkesh",
#     "city": "FBD",
#     "age": 25
# }
#
# userInfo.popitem()
#
# Output:
# ('age', 25)
#
# Dictionary becomes:
# {
#     "name": "Rinkesh",
#     "city": "FBD"
# }
#
# ==========================================
# Difference Between pop() and popitem()
# ==========================================
#
# pop(key)
# - Removes a specific key.
# - Returns the value only.
#
# Example:
# userInfo.pop("name")
# Output:
# "Rinkesh"
#
#
# popitem()
# - Removes the last inserted item.
# - Returns both key and value as a tuple.
#
# Example:
# userInfo.popitem()
# Output:
# ('age', 25)
#
# ==========================================
# Important
# ==========================================
#
# Python dictionaries maintain insertion order.
# Therefore, popitem() always removes the most recently added item.
#
# If the dictionary is empty:
#
# emptyDict = {}
# emptyDict.popitem()
#
# Output:
# KeyError: 'popitem(): dictionary is empty'





# ==========================================
# del Statement with Dictionary
# ==========================================

# del is used to delete a specific key-value pair
# from a dictionary.

del userInfo["isMarried"]

# Print the dictionary after deletion
print(userInfo)

# ==========================================
# Notes
# ==========================================
#
# Syntax:
# del dictionary[key]
#
# Purpose:
# Removes the specified key and its value from the dictionary.
#
# Example:
#
# userInfo = {
#     "name": "Rinkesh",
#     "city": "FBD",
#     "isMarried": False
# }
#
# del userInfo["isMarried"]
#
# Result:
# {
#     "name": "Rinkesh",
#     "city": "FBD"
# }
#
# ==========================================
# Important
# ==========================================
#
# If the key does NOT exist,
# Python raises a KeyError.
#
# Example:
#
# del userInfo["salary"]
#
# Output:
# KeyError: 'salary'
#
# ==========================================
# Safe Ways to Delete a Key
# ==========================================
#
# Method 1: Check before deleting
#
# if "salary" in userInfo:
#     del userInfo["salary"]
#
#
# Method 2: Use pop() with a default value
#
# userInfo.pop("salary", None)
#
# This will:
# - Remove the key if it exists.
# - Return None if it does not exist.
# - NOT raise an error.
#
# ==========================================
# Difference Between del and pop()
# ==========================================
#
# del userInfo["key"]
# - Deletes the key.
# - Does NOT return the value.
# - Raises KeyError if key is missing.
#
#
# userInfo.pop("key")
# - Deletes the key.
# - Returns the deleted value.
# - Raises KeyError if key is missing.
#
#
# userInfo.pop("key", None)
# - Deletes the key if present.
# - Returns None if key is missing.
# - Does NOT raise an error.



userInfo2 = userInfo.copy()
print(userInfo2,userInfo)




