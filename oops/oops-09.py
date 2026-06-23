# ==========================================
# Python OOP Notes: @staticmethod, @classmethod, @property
# ==========================================

# ------------------------------------------
# 1. @staticmethod
# ------------------------------------------
# A method that belongs to the class but does not
# access instance variables (self) or class variables (cls).

class Employee:

    @staticmethod
    def company_info():
        return "Company established in 2010"


# Usage:
Employee.company_info()

# Use when:
# - Method is related to the class
# - Does not need self or cls
# - Utility/helper functions

# ------------------------------------------
# 2. @classmethod
# ------------------------------------------
# A method that receives the class itself as
# the first argument (cls).

class Employee:
    total_employee = 0

    @classmethod
    def get_total_employee(cls):
        return cls.total_employee


# Usage:
Employee.get_total_employee()

# Internally:
# Employee.get_total_employee(Employee)

# cls refers to the class object itself.

# Use when:
# - Working with class variables
# - Creating alternative constructors
# - Supporting inheritance

# self  -> current object
# cls   -> current class

# ------------------------------------------
# 3. @property
# ------------------------------------------
# Allows a method to be accessed like a variable.

class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def employeeName(self):
        return f"Employee Name: {self.__name}"


emp = Employee("Rinkesh")

# Usage:
print(emp.employeeName)

# NOT:
# print(emp.employeeName())

# Use when:
# - You want method-like logic
# - But want variable-like access
# - Creating read-only attributes
# - Adding validation/calculations later

# ------------------------------------------
# Quick Comparison
# ------------------------------------------

# Instance Method
# def show(self):
#     pass
#
# Access:
# obj.show()
#
# Can use:
# self.name

# Class Method
# @classmethod
# def show(cls):
#     pass
#
# Access:
# Employee.show()
#
# Can use:
# cls.total_employee

# Static Method
# @staticmethod
# def show():
#     pass
#
# Access:
# Employee.show()
#
# Cannot use:
# self or cls

# Property
# @property
# def name(self):
#     return self.__name
#
# Access:
# obj.name
#
# Looks like a variable but runs a method.

# ------------------------------------------
# Memory Trick
# ------------------------------------------
# self  -> Current Object
# cls   -> Current Class
# staticmethod -> Neither Object nor Class
# property -> Method behaves like Variable
# ------------------------------------------