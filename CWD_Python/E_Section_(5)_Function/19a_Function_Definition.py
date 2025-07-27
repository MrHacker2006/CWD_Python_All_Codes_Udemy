 
# def average(a,b,c):
#     d = (a+b+c)/3
#     print(d)

# print("Printing the value without using return")
# average(1,2,3)
# average(2,6,9)
# print("\n")


'''This will not work directly, for this you have use return'''

def average(a,b,c):
    d = (a+b+c)/3
    # print(d)
    return d
print("Printing the value using return")
x1 = average(1,2,3)
x2 = average(2,6,9)
print(x1)
print(x2)