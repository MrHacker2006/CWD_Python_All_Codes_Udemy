numbers = [1,2,5,89,34,45,78,23,26,78,18,9,6,20]

def number_greater_than_9(x):
    if x > 25:
        return True
    else:
        return False
    

# a = list(filter(number_greater_than_9, numbers))
# print(a)

''' We can get same output using Lambda Function'''
b = list(filter(lambda x: x>25, numbers))
print(b)
