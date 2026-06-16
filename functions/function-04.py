def multiply(a, b):
    if (
        isinstance(a, (int, float)) and isinstance(b, (int, float))
    ) or (
        isinstance(a, str) and isinstance(b, int)
    ) or (
        isinstance(a, int) and isinstance(b, str)
    ):
        return a * b

    return "Invalid inputs"


# Number × Number
print(multiply(1, 1))    # 1
print(multiply(2, 3))    # 6
print(multiply(5, 5))    # 25
print(multiply(10, 15))  # 150
print(multiply(15, 15))  # 225

# String × Number
print(multiply("A", 1))   # A
print(multiply("A", 3))   # AAA
print(multiply("Hi", 5))  # HiHiHiHiHi
print(multiply("*", 10))  # **********
print(multiply("-", 15))  # ---------------

# Number × String
print(multiply(1, "A"))   # A
print(multiply(3, "A"))   # AAA
print(multiply(5, "Hi"))  # HiHiHiHiHi
print(multiply(10, "*"))  # **********
print(multiply(15, "-"))  # ---------------

# Edge Cases
print(multiply(0, 5))     # 0
print(multiply(5, 0))     # 0
print(multiply("", 5))    # (empty string)
print(multiply("Hi", 0))  # (empty string)
print(multiply(-2, 3))    # -6

print(multiply("a","b"))