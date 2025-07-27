class employee():
    Company = "HCL"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    # '''Instance method(default)'''
    def print_info(self):
        return f"The Name of the employee {self.position} : {self.name}\nThe salary of the employee {self.position} : {self.salary}"
    
    # def sum(self,a,b):
    def sum(a,b):
        return a+b


e1 = employee("Gautam", 34000,1)
e2 = employee("Gaurav", 34001,2)

print(employee.Company)
print(e1.Company)
print(e1.Company)

# Both will throw an error
# print(employee.name)   
# print(employee.salary)

print(e1.print_info())
print(e2.print_info())

#It will throw an error , if i try it to run without using self
# TypeError: employee.sum() takes 2 positional arguments but 3 were given

# So, if i want to access the sum() function without using self parameter, then for that i have to use static method

# print(e1.sum(4,8)) 