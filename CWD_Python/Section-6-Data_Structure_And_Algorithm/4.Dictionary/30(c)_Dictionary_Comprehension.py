#Printing the table of 5
n = int(input("Enter the number for which you want table:"))
table = { i : n*i for i in range(1,11)}
print(table)



# Printing the squares of numbers till 10
squares = {x: x**2 for x in range(11)}
print(squares)