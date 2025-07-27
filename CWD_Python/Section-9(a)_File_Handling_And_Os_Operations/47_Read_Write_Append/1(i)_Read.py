f = open("Gautam1.txt", "r")
# f = open("Gautam.txt", "r")   #This will throw an error , because the file which we are trying to open that doesn't exist.

content = f.read()

print(content)

f.close()