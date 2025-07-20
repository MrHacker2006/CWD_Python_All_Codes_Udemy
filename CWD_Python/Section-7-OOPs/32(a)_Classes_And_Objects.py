
class Employee:
    Company = "HCL"

    def get_salary(self):
        return 34000


e1 = Employee()
print(e1.Company)
print(e1.get_salary())

e2 = Employee()
print(e2.get_salary())