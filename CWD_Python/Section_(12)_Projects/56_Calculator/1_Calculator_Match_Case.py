num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
opera = int(input("Enter 1 for add\nEnter 2 for subtratction\nEnter 3 for Multiplication\nEnter 4 for division\n"))
# oper = ['add','sub','mul','div']
try:
    match opera:
     case 1:
        print(f"The additon of num1 and num2 is {num1 + num2}")
     case 2:
        print(f"The subtration of num1 and num2 is {num1 - num2}")
     case 3:
        print(f"The multiplication of num1 and num2 is {num1*num2}")
     case 4:
        print(f"The division of num1 and num2 is {num1/num2}")
     case default:
        print("Something gone wrong!")
except ZeroDivisionError:
   print("Division by zero of any number is not possible.")
except Exception as e:
   print("Unknown Error occured!") 