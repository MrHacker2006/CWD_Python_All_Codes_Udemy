# When we are using with, we don't have to use f.close(), it automatically closses the file

with open("Gautam1.txt", "r") as f:
    
    content = f.read()

    print(content)
