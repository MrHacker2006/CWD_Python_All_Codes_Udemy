# Now let's Modify the program
'''As you can see , normal print function is not working here.'''


def divide(a,b):

    try:
        c=a/b
        print(c)
        return c

    except Exception as e:
        print("Error Occured!: ",e)
        return None
    
    # finally:
    #     print("It will be always executed, whether program gives an error or not.")

    # print("It will be always executed, whether program gives an error or not.")

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
divide(a,b)