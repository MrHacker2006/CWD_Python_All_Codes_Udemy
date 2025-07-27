import os 

f = os.open("Radhe.txt", os.O_WRONLY)

os.write(f, b"Hello, World!")

os.close(f)
