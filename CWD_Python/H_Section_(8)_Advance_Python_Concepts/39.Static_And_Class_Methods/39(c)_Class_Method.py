class employee():
    Company = "HCL"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    # '''Instance method(default)'''
    def print_info(self):
        return f"The Name of the employee {self.position} : {self.name}\nThe salary of the employee {self.position} : {self.salary}"
    
    # Class methods
    @classmethod
    def print_company(cls):
       print(cls.Company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.Company = new_company


e1 = employee("Gautam", 34000,1)
e2 = employee("Gaurav", 34001,2)

# e1.print_company()

print(employee.Company)
e1.change_company("Google")
print(employee.Company)   #It is actually changing the company of the class attribut(Company)