class Employee:
    def __init__(self,name,work):
        self.name= name
        self.work=work
    
    def printInfo(self):
        return f"Name:{self.name} Designation:{self.work}"



class EmployeeExperience(Employee):
    def __init__(self,name,work,yearOfExperience):
                super().__init__(name,work)
                self.yearOfExperience = yearOfExperience




employeeOne = Employee("Rinkesh","Full Stack Developer")
employeeTwo = Employee("Abhishek","PM")


print(employeeOne)
print(employeeTwo)
print(employeeOne.name,employeeOne.work)
print(employeeTwo.name,employeeTwo.work)
print(employeeOne.printInfo())
print(employeeTwo.printInfo())

print("=======================================================================")

employeeThree = EmployeeExperience("Aditya","CEO",22)
print(employeeThree.name,employeeThree.work,employeeThree.yearOfExperience)
print(employeeThree.printInfo())