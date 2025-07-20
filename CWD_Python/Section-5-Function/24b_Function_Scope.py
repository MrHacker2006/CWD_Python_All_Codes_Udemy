def sum(a,b):
    global z # it will modify global z
    z=5 #This is a Local Variable
    return a+b
 
z=2 # This is a Global Variable
print(sum(21,3)) 
print(z) 
'''This is now printing the local z variable because we have used the global keyword inside the funciton'''
