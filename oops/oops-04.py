class Employee:
    def __init__(self,name,work):
        self.name= name
        # this work will become private
        self.__work=work
    
    def printInfo(self):
        return f"Name:{self.name} Designation:{self.__work}"
    
    def get_work_info(self):
        return f"Work:{self.__work}"



class EmployeeExperience(Employee):
    def __init__(self,name,work,yearOfExperience):
                super().__init__(name,work)
                self.yearOfExperience = yearOfExperience
                
                
    def printFullDetails(self):
        return f"{self.name}, {self._Employee__work}, {self.yearOfExperience}"            




employeeOne = EmployeeExperience("Aditya","CEO",22)
print(employeeOne.name,employeeOne.yearOfExperience)
# print(employeeOne.work)
# print(employeeOne.__work)
# print(employeeOne._Employee__work)
# print(employeeOne._EmployeeExperience__work)
print(employeeOne.printInfo())
print(employeeOne.printFullDetails())
print(employeeOne.get_work_info())