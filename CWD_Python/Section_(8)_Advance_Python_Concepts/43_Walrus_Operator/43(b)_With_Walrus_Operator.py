def very_slow_func():
    print("Something is going to execute.......")
    print("Something is going to execute.......")
    # return 9 
    return 11  

''' It will execute the function one time'''
a = very_slow_func()  
if(a>10):
    print(a)
else:
    print("Number is not greater than 10")

'''Both are giving same output'''
if((b:=very_slow_func())>10):
    print(b)
else:
    print("Value is not greater than 10")