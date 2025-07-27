while True:
    try:
        a = int(input("Enter Number 1: "))
        b = int(input("Enter Number 2: "))
        print(f"The division is {a/b}")


    except ValueError:
        print("Please don't perform bad typecast")

    except ZeroDivisionError:
        print("Division by Zero is not possible")

    # It will stop program from terminating in case of inappropriate value entered by the user

    # except:
    #   or
    except Exception as e:                  
        print("Unknown error occured!: ", e)






