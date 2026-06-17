# ==========================================
# PYTHON NOTES: VARIABLE SCOPE
# ==========================================

# 1. GLOBAL SCOPE
# Variables created outside a function belong to the global scope.

name = "Rinkesh"

print(name)  # Accessible anywhere in the file


# ------------------------------------------
# 2. LOCAL SCOPE
# Variables created inside a function belong
# to the local scope and exist only while
# the function is executing.
# ------------------------------------------

def test():
    name = "Rinkesh Kumar"
    print(name)

test()

# print(name) outside the function would access
# the global variable, not the local one.


# ------------------------------------------
# 3. FUNCTION SCOPE VS BLOCK SCOPE
# ------------------------------------------

# Python creates a new scope for:
# - Functions (def)
# - Classes (class)
# - Modules (files)

# Python DOES NOT create a new scope for:
# - if
# - for
# - while
# - try

if True:
    a = 10

print(a)  # Works because if-block does not create scope


# ------------------------------------------
# 4. EXAMPLE
# ------------------------------------------

name = "Rinkesh"

def test():
    name = "Rinkesh Kumar"
    print(name)

    if True:
        a = "this is a"
        print(a)

    print(a)

test()
print(name)

# Output:
# Rinkesh Kumar
# this is a
# this is a
# Rinkesh

# Explanation:
# - Local 'name' inside function shadows global name.
# - Variable 'a' is accessible throughout the function.
# - Global 'name' remains unchanged.


# ------------------------------------------
# 5. ACCESSING GLOBAL VARIABLES
# ------------------------------------------

name = "Rinkesh"

def show_name():
    print(name)

show_name()

# Output:
# Rinkesh


# ------------------------------------------
# 6. MODIFYING GLOBAL VARIABLES
# ------------------------------------------

count = 10

def update_count():
    global count
    count = 20

update_count()
print(count)

# Output:
# 20

# Use the 'global' keyword when you want
# to modify a global variable inside a function.


# ------------------------------------------
# 7. PYTHON VARIABLE LOOKUP (LEGB RULE)
# ------------------------------------------

# Python searches variables in this order:

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# Example:

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()

# Output:
# Local


# ------------------------------------------
# INTERVIEW NOTES
# ------------------------------------------

# Scope Types:
#
# 1. Global Scope
#    - Defined outside functions.
#
# 2. Local Scope
#    - Defined inside functions.
#
# 3. Enclosing Scope
#    - Defined in outer functions.
#
# 4. Built-in Scope
#    - Python's predefined functions and variables.


# ------------------------------------------
# IMPORTANT RULES TO REMEMBER
# ------------------------------------------

# ✅ Functions create a new scope.

def example():
    x = 10


# ❌ if/for/while blocks do NOT create a new scope.

if True:
    y = 20

print(y)  # Works


# ------------------------------------------
# MEMORY TRICK
# ------------------------------------------

# "Functions create scope,
#  if/for/while do not create scope."
#
# Python follows LEGB:
# Local → Enclosing → Global → Built-in
# ==========================================