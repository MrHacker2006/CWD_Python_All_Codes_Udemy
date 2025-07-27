a = int(input("Enter the number 1:" ))
b = int(input("Enter the number 2:" ))


# Benefit of raising error is that the program is getting crashsed , and the user is not able to proceed further.

#This is custom error
if b== 0 :
    raise ValueError("Divison by Zero is not possibleeeeee")

print(f"The division is {a/b}")
