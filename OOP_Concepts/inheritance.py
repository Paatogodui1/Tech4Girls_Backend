#Creating a parent class Employee
class Employee: 
    def __init__(self, name, position): 
        self.name = name 
        self.position = position 
        
    def get_details(self): 
            print(f"Employee Name: {self.name}") 
            print(f"Position: {self.position}") 

#Child class Manager that inherits from Employee 
class Manager(Employee): 
    def __init__(self, name, position, department): 
        super().__init__(name, position) 
        self.department = department 
        
    def get_details(self): 
            super().get_details() 
            print(f"Department: {self.department}") 
            
#Creating an instance of Employee 
employee1 = Employee("Habiba Adams", "Software Engineer") 

#Creating an instance of Manager 
manager1 = Manager("Ophebea Iris", "Project Manager", "Margins Group") 

#Calling get_details() 
print("Employee Details:") 
employee1.get_details() 
print("\nManager Details:") 
manager1.get_details()