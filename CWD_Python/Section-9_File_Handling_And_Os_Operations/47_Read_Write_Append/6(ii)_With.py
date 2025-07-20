try:
    with open("Gautam2.txt", "r") as f:

     content = f.read()

    print(content)

except FileNotFoundError:
   print("File Not Found.")

with open("Gautam2.txt", "w") as f:
   f.write("This is written at the time of using with statement 2nd time")
   