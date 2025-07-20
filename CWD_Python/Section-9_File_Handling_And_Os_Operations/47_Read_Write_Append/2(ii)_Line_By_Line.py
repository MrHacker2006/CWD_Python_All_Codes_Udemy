try:
    f = open("Gautam1.txt", "r")

    for line in f:
        print(line.strip()) # Remove Newline Characters
    
    f.close()
except FileNotFoundError:
    print("File Doesn't Exist")