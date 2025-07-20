# Creating a list which contain the table of 5

# Way-1
# table =[]
# for i in range(1,11):
#     table.append(5*i)
# print(table)

# Way-2 --> Using list comprehension

table =[5*i for i in range(1,11)]
print(table)