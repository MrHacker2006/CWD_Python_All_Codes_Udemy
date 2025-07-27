try:
    # a = 345/0
    a = 345/10
    print(a)
except Exception as e:
    print("Error Occured!:" , e)

# it is used when we want to make sure that there is no error in the try block
else:
    print("It simply means that you want to print something whenever there is no error in the try block.")  
    