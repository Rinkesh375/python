# ==========================================
# PYTHON SHORT NOTES: LEGB & SCOPE
# ==========================================

# Local Scope
# - Variable created inside a function.
# - Accessible only inside that function.

def test():
    name = "Rinkesh"   # Local Variable


# Enclosing Scope
# - Variable created in an outer function.
# - Accessible by inner (nested) functions.

def outer():
    city = "Delhi"     # Enclosing Variable

    def inner():
        print(city)


# Global Scope
# - Variable created outside all functions.
# - Accessible throughout the file.

name = "Rinkesh"       # Global Variable


# Built-in Scope
# - Variables/functions provided by Python.
# - Examples: print(), len(), type(), input()


# LEGB Rule
# Python searches variables in this order:
#
# L → Local
# E → Enclosing
# G → Global
# B → Built-in


# Example

name = "Global"

def outer():
    city = "Delhi"      # Enclosing

    def inner():
        age = 28        # Local
        print(age, city, name)

    inner()

outer()

# Output:
# 28 Delhi Global


# Important Rule
# ✅ Functions create scope
# ❌ if, for, while do NOT create scope


# Memory Trick
# Local     = Current Function
# Enclosing = Parent Function
# Global    = Outside Functions
# Built-in  = Python's own functions