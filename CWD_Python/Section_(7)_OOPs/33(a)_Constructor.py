class Employee:

    def __init__(self,salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}, His salary is {self.salary} and its bond is {self.bond} years")

    
e1 = Employee(3400000, "Gautam" , 4)
print(e1.get_salary())
e1.get_info()