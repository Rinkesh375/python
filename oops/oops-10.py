class Employee:
    total_employee = 0
    def __init__(self,name,work):
        self.name= name
        # this work will become private
        self.__work=work
        Employee.total_employee += 1
    
    def printInfo(self):
        return f"Name:{self.name} Designation:{self.__work}"
    
    def get_work_info(self):
        return f"Work:{self.__work}"
    
    def work_mode(self):
        return f"{self.name} Work from office"
    
    @staticmethod
    def company_info():
        return "Company is protoezy established in 2010"



class EmployeeExperience(Employee):
    def __init__(self,name,work,yearOfExperience):
                super().__init__(name,work)
                self.yearOfExperience = yearOfExperience
                
                
    def printFullDetails(self):
        return f"{self.name}, {self._Employee__work}, {self.yearOfExperience}"
    
    
    def work_mode(self):
        return f"{self.name} Work from Home"            



employeeOne = Employee("Rinkesh","Developer")
employeeTwo = EmployeeExperience("Aditya","CEO",22)

print(isinstance(employeeOne,Employee))
print(isinstance(employeeOne,EmployeeExperience))



print(isinstance(employeeTwo,Employee))
print(isinstance(employeeTwo,EmployeeExperience))