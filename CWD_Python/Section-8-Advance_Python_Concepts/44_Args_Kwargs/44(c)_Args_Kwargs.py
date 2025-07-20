def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(99,3,3,44, Gautam=100, Gaurav=89)

# func1(99,Gautam=100 ,88)  # It will throw an error