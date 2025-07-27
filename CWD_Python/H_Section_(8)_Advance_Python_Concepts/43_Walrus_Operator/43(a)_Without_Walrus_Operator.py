def very_slow_func():
    print("Something is going to execute.......")
    print("Something is going to execute.......")
    # return 9  # at this condition both will execute the very_slow_func() one time
    return 11   # at this condition one will execute the very_slow_func() twice and the other will execute it only once

'''By calling it like this, its will execute the function'''
# if(very_slow_func()>10):   
#     print(very_slow_func())
# else:
#     print("Value is not greater than 10")

'''But when we execute it like this, it will be only executed one time, when the condition is true'''
a = very_slow_func()
if(a>10):
    print(a)
else: 
    print("Value is not greater than 10")