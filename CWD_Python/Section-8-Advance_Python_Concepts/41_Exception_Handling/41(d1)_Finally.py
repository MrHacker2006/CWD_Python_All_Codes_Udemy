# THis program is created due to an reason, think that if there will be no finally and there is just print statement in its place , it will still works the same, when the program is normal, but when we modify it, it will not work let me show you

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

try:
    c=a/b
    print(c)

except Exception as e:
    print(e) 
 
# finally:    
#     print("It will be always executed, whether program gives an error or not.")

# As you can see here, when program is not modified it is working as same as the finally.
print("It will be always executed, whether program gives an error or not.")