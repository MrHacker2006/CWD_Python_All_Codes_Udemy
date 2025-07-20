from functools import reduce

numbers = [1,2,3,4,5,6]

def sum(a,b):
    return a+b

a = reduce(sum , numbers)
print(a)


b = reduce(lambda x,y : x+y , numbers)
print(b)