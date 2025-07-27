try:
    f = open("Gautam2.txt", "w")
    # If we change the content inside the string it will be overwritten on the existing content of the file
    str = "Focus on Goals not on Holes."

    f.write(str)

    f.close()
except FileNotFoundError:
    print("File Not Found.")