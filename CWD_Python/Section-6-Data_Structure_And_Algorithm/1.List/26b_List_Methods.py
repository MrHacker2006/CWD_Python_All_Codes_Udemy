print("="*50)
print("List Methods")
print("="*50)

col = ['voilet', 'indigo', 'blue','green','blue']

print("\n5.list.copy()") 
newlist = col.copy()
print(col)
print(newlist)


col = ['voilet', 'indigo', 'blue','green','blue']

print("\n6.list.append()") 
col.append("red")
print(col)

#         0        1         2       3       4
col = ['voilet', 'indigo', 'blue','green','blue']

print("\n7.list.insert()") 
col.insert(2,"grey")
print(col)


col = ['voilet', 'indigo', 'blue','green','blue']
# ors = ['magenta','white', 'pink']     # list
ors = ('magenta','white', 'pink')       # tuple

print("\n8.list.extend()") 
col.extend(ors)
print(col)



# we can simply concatenate two list with the help of + (addition symbol)
num1= [1,3,5,7,9]
num2= [2,4,6,8,10]

a=(num1+num2)
a.sort()