# Decorator is a function that takes a function, it creates a new function inside its body (wrapper) . Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("Function is executed sucessfully....")
    return wrapper


# Way-1 of Calling Decorators

def say_hello():
    print("Hello!")

f= decorator(say_hello)
f()

'''
f will look like something this
def f():
   print("I am about to execute a function....")
   func()
   print("Function is executed sucessfully....")
'''