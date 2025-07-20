'''Due to immutability tuple don't have methods like list, they have very very less'''

t1 = (2 , 3, 4, 55, 3, 23, 54, 67, 3, 3)
#     0   1  2  3   4  5   6   7   8  9
print(t1.count(3))
print(t1.index(4))
print(t1.index(3))

