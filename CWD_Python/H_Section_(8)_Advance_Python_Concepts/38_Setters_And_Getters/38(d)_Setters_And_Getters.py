class Employee:

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
     
    @property
    def first_name(self):
        str = self.name.split(" ")
        return str[0]
    

    @first_name.setter
    def first_name(self,first):        
        str = self.name.split(" ")
        new_name = f"{first} {str[1]} "
        self.name = new_name


e1= Employee("Jack Doe", 6000)

print(e1.name)

e1.first_name = "Gautam"
print(e1.name)


