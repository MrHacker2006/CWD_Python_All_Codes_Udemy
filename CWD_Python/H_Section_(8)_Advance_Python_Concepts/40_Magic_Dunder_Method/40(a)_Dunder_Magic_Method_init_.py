class Employee:
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary

e = Employee("Gautam", 60000)

print(e.name, e.salary)