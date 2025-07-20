import argparse

parser = argparse.ArgumentParser(description="A simple command line utility.")

parser.add_argument("filename", help="The file to process")
parser.add_argument("-n", "--number",type=int, default=1, help="Enter any valid number")

args = parser.parse_args()

print(args)

try:
    with open(args.filename, "r") as f:
     content = f.read()
     for _ in range(args.number):
        print(content)
except FileNotFoundError:
    print("File does not exist!")
# In Python, the underscore _ is a convention that means:
# "I'm intentionally ignoring this value."


#   python 4_Command_Line_Simple.py F1.txt -n 8
#   python 4_Command_Line_Simple.py F1.txt         # it will take 1 by itself, because 1 is the default value