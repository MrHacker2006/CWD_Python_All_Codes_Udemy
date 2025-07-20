class Employee:
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary
    
    def __len__(self):
        return len(self.name)

e = Employee("Gautam", 60000)

print(len(e))
