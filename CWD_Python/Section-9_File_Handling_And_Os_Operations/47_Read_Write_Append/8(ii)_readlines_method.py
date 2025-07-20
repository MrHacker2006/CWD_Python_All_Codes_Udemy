f = open("Gautam1.txt", 'r')

while True:
    line = f.readlines()
    if not line:
        break
    print(line)