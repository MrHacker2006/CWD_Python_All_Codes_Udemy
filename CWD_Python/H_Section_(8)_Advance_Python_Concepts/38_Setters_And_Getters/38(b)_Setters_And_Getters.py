class Employee:

    def __init__(self, name , salary):
         self.name = name
         self.salary = salary
    
    def first_name(self):
         str = self.name.split(" ")
         print(str)
         return str[0]


e1 = Employee("John Doe", 6000)

print(e1.first_name())


