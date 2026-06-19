class Employee:
    def __init__(self,name,work):
        self.name= name
        self.work=work
    

    def printInfo(self):
        return f"Name:{self.name} Designation:{self.work}"


employeeOne = Employee("Rinkesh","Full Stack Developer")
employeeTwo = Employee("Abhishek","PM")

print(employeeOne)
print(employeeTwo)
print(employeeOne.name,employeeOne.work)
print(employeeTwo.name,employeeTwo.work)
print(employeeOne.printInfo())
print(employeeTwo.printInfo())