file = open("./example.py")


# for i in range(10):
#     print(i, print(file.__next__()))







print(file.__next__())


print(file.__next__())

print(file.__next__())

print(file.__next__())
print(file.__next__())
print(file.__next__())
print(file.__next__())

print(file.__next__())
print(file.__next__())

print(file.__next__())

print(file.__next__())
print(file.__next__())
print(file.__next__())

print(file.__next__())




# ==========================================
# __next__() and StopIteration Notes
# ==========================================

# file.__next__()
# Returns the next line from a file.

# Example:
# file = open("example.py")
# print(file.__next__())

# When there are no more lines left,
# __next__() raises a StopIteration exception.

# Example:
#
# file = open("example.py")
#
# while True:
#     print(file.__next__())
#
# Output:
# StopIteration

# for loops automatically handle StopIteration.

# Example:
#
# for line in file:
#     print(line)
#
# Internally similar to:
#
# while True:
#     try:
#         line = file.__next__()
#         print(line)
#     except StopIteration:
#         break

# next(file) and file.__next__() are equivalent.

# Summary:
# __next__() -> Get next item
# StopIteration -> No more items available
# for loop -> Automatically catches StopIteration
# Manual __next__() -> Must handle StopIteration yourself