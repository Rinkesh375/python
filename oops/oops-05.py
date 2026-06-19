# ==========================================
# PYTHON OOP NOTES: PRIVATE VARIABLES
# ==========================================

# Public Variable
# - Accessible from anywhere.

class Employee:
    def __init__(self, name, work):
        self.name = name      # Public
        self.work = work      # Public

emp = Employee("Aditya", "CEO")

print(emp.name)   # Aditya
print(emp.work)   # CEO


# ==========================================
# PRIVATE VARIABLE (__variable)
# ==========================================

class Employee:
    def __init__(self, name, work):
        self.name = name
        self.__work = work    # Private Variable


emp = Employee("Aditya", "CEO")

# print(emp.__work)   # AttributeError

# Python performs Name Mangling:
# __work becomes _Employee__work

print(emp._Employee__work)    # CEO (Not Recommended)


# ==========================================
# WHY employeeOne.work DOES NOT WORK
# ==========================================

class Employee:
    def __init__(self, name, work):
        self.name = name
        self.__work = work


emp = Employee("Aditya", "CEO")

# print(emp.work)

# Error:
# AttributeError:
# 'Employee' object has no attribute 'work'

# Because:
# self.work was never created.
# Only self.__work exists.


# ==========================================
# WHY employeeOne.__work DOES NOT WORK
# ==========================================

class Employee:
    def __init__(self, name, work):
        self.__work = work


emp = Employee("Aditya", "CEO")

# print(emp.__work)

# Error:
# AttributeError

# Because Python changed:
# __work -> _Employee__work


# ==========================================
# ACCESS PRIVATE VARIABLE USING GETTER
# ==========================================

class Employee:
    def __init__(self, name, work):
        self.name = name
        self.__work = work

    def get_work(self):
        return self.__work


emp = Employee("Aditya", "CEO")

print(emp.get_work())   # CEO


# ==========================================
# PRIVATE VARIABLE INSIDE CLASS
# ==========================================

class Employee:
    def __init__(self, name, work):
        self.name = name
        self.__work = work

    def printInfo(self):
        return f"Name: {self.name}, Designation: {self.__work}"


emp = Employee("Aditya", "CEO")

print(emp.printInfo())

# Output:
# Name: Aditya, Designation: CEO

# Works because methods inside the class
# can access private variables directly.


# ==========================================
# INTERVIEW NOTES
# ==========================================

# self.work
# -> Public Variable

# self._work
# -> Protected Variable (Convention Only)

# self.__work
# -> Private Variable (Name Mangling)

# Python changes:
# __work -> _ClassName__work

# Example:
# self.__work
# becomes
# self._Employee__work


# ==========================================
# MEMORY TRICK
# ==========================================

# work      -> Public
# _work     -> Protected
# __work    -> Private

# Public    -> Access Anywhere
# Protected -> Should Not Access Outside (Convention)
# Private   -> Name Mangling Applied
#
# __work becomes _Employee__work internally.
# ==========================================