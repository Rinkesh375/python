class Employee:
    total_employee = 0
    def __init__(self,name,work):
        self.__name= name
        # this work will become private
        self.__work=work
        Employee.total_employee += 1
    
    def printInfo(self):
        return f"Name:{self.__name} Designation:{self.__work}"
    
    def get_work_info(self):
        return f"Work:{self.__work}"
    
    def work_mode(self):
        return f"{self.__name} Work from office"
    
    @staticmethod
    def company_info():
        return "Company is protoezy established in 2010"
    
    @property
    def employeeName(self):
        return f"Employee Name:{self.__name}"


           



employeeOne = Employee("Rinkesh","Developer")


print(employeeOne.work_mode())

print(f"Total Employee created {Employee.total_employee}")


print(employeeOne.company_info())
print(Employee.company_info())

print(employeeOne.employeeName)