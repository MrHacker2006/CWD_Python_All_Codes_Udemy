numbers = [1,2,3,4,5,6,7,8]

# def squares(x):
#     return x*x

# # Ii will return the object , for getting list we have to typecast it.
# a = map(squares, numbers)

# a = list(map(squares, numbers))
# print(a)

'''We can directly use lambda function'''

b = list(map(lambda x: x*x, numbers))
print(b)