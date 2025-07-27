num = int(input("Enter any number :"))

match num:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case 4:
        print("Number is 4")
    case 5:
        print("Number is 5")
    case _:
        print("The number you have entered is not between 1 and 5")

# match num:
#     case 0: 
#         print("num is zero")
#     case 4 if num%2==0:
#         print("num%2 == 0 and case is 4")
#     case _ if num<10:
#         print("num is <10")
# print(num)