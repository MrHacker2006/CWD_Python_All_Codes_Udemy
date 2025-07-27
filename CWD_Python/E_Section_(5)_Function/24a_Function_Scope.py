def sum(a,b):
    z=5 #This is a Local Variable
    return a+b
 
z=2 # This is a Global Variable
print(sum(2,3)) 
print(z) 

'''It is printing global variable because when we call an function, its after performing its opeartion destroys all its local variable, that's why we can't access the value of local variable normally'''