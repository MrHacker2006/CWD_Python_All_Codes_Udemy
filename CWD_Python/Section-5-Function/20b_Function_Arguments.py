'''Default Argument'''

def average(a, b, sum=8):
    c = (a+b+sum)/3
    return c

a1= average(2,2)   #12/3
print(a1)

a2 = average(2,4,2)   #8/3    #Default argument value will be overwritten
print(a2)