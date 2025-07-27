class Employee:
    Company ="HCL"                                 #   This is class attribute

    def __init__(self,salary, name, bond, Company): #  Here, Company--> instance attribute 
        self.salary = salary
        self.name = name
        self.bond = bond
        self.Company = Company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}, His salary is {self.salary} and its bond is {self.bond} years")


e1 = Employee(340000, "Gautam", 3, "TESLA")
print(e1.Company)  # It will always print instance attribute, it is present otherwise it will print the class attribute

print(Employee.Company) # It will always print the class attribute


'''Object Introspection''' # It is way to find all the methods that a particular object in python has
print(dir(e1))