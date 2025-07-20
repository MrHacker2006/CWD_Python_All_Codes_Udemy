print("="*50)
print("List Methods")
print("="*50)

col = ['voilet', 'indigo', 'blue','green']
num = [4,2,5,3,6,1,2,1,2,8,9,7]

print("\n1a.list.sort()") #This will print the list in ascending order(chote se bada)
# print(col.sort())       # This is giving error, i don't know why?
print(col)
num.sort()
print(num)


print("\n1b.list.sort()")
col.sort(reverse=True)
print(col)
num.sort(reverse=True)
print(num)


col = ['voilet', 'indigo', 'blue','green']
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print("\n2.list.reverse()") #This will print the list in ascending order(chote se bada)
col.reverse()
print(col)
num.reverse()
print(num)


col = ['voilet', 'indigo', 'blue','green']
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print("\n3.list.index()") #This will print the list in ascending order(chote se bada)
print(col.index("blue"))
print(num.index(1))


col = ['voilet', 'indigo', 'blue','green','blue']
num = [4,2,5,3,6,1,2,1,2,8,9,7]
print("\n4.list.count()") #This will print the list in ascending order(chote se bada)
print(col.count("blue"))
print(num.count(1))
