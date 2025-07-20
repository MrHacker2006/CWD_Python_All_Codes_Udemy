
print("11a.find()")
s1= "Apple Mango Pineapple Guavava"
print(s1.find("Mango"), "\n")
print("11b.find()")           # The searched word is not present, but it is not giving any error, but index() method will give the error
s2= "Apple Mango Pineapple Guavava"
print(s2.find("is"), "\n")


print("12a.index()")
s3= "Apple Mango Pineapple Guavava"
print(s3.index("Mango"), "\n")

'''It will throw error, because "is" is missing'''
# print("12b.index()")   
# s4= "Apple Mango Pineapple Guavava"
# print(s4.index("is"), "\n")


print("13a.isalnum()")   
s5= "YouAreLooking(10/10)"
print(s5.isalnum(), "\n")
print("13b.isalnum()")   
s6 = "YouAreLookingGood"
print(s6.isalnum(), "\n")



print("14a.isalpha()")   
s7= "YouAreLooking(10/10)"
print(s7.isalpha(), "\n")
print("14b.isalpha()")   
s8 = "YouAreLookingGood"
print(s8.isalpha(), "\n")
