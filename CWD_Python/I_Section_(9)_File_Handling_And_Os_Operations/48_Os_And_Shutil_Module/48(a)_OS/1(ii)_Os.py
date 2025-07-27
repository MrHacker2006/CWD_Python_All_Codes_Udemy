import os

'''Reading an file'''

#Opening file in read only mode
f = os.open("Radhe.txt", os.O_RDONLY)

content = os.read(f,1024)  #1024 bytes = 1 kb
print(content)
os.close(f)