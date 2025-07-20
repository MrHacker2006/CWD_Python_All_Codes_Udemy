class Employee:

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
     
    def first_name(self):
        str = self.name.split(" ")
        return str[0]
    
    # This function can change the first name
    def set_first_name(self,first):
        str = self.name.split(" ")
        new_name = f"{first} {str[1]} "
        self.name = new_name


e1= Employee("Jack Doe", 6000)

e1.set_first_name("Gautam")
print(e1.name)