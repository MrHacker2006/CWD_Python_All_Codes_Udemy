def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("Function is executed sucessfully....")
    return wrapper


# Way-2 Of Calling Function

@decorator
def say_hello():
    print("Hello!")

say_hello()


