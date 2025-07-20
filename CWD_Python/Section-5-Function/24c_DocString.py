def sum(a,b):
    '''This is a Comment which is written with the help of multiline string. When a Multiline string is written just inside the(on first line) function, it is considered as DocStrings. Which can be accessed using print(functionName.__doc__)'''
    c=a+b
    return c

print(sum.__doc__)
