s1 = "This is a String"
print("1.upper()")
print(s1.upper(), "\n")



s2 = "THIS IS A JOKE"
print("2.lower()")
print(s2.lower(), "\n")



s3 ="  \nYou are Very Brilliant Man!  "
print("3.strip()")
print(s3.strip(), "\n")
# print(s3)



'''rstrip()'''
print("4.rstrip()")
s4 = "1,2,3,,,,,"  # trailing comma
print(s4.rstrip(","))

s5 = "123.34400000"
print(s5.rstrip("0"))

s6 = "Don't Go Ahead!!! @@@@"
# print(s6.rstrip("!","@"))   '''We can't give two arguments inside the rstrip()'''
print(s6.rstrip("@"))   # Only the outer side unwanted characters can be removed, you can't remove both
