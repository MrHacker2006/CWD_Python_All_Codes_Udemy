class Employee:
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary
    
    #This is mostly used for showing infromation to the users
    #informal string representation of the object
    def __str__(self):
        return f"The name of the employee is {self.name}, and the salary of the employee is {self.salary}."
    
    #This is mostly used for representing information to the developers
    #formal string representation of the object
    def __repr__(self):
        return f"Name:{self.name}\nSalary:{self.salary}"

e = Employee("Gautam", 60000)

print(str(e))

print(repr(e))
