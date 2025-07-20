f = open("Gautam2.txt", "w")

lines = ['line1', 'line2', 'line3']

for line in lines:
    f.write(line + "\n")

f.close()