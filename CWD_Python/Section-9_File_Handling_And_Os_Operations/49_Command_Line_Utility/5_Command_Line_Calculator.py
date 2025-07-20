import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation",choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()
# It reads the arguments passed via command line (like: python 1_Command.py 5 10 add)
# If all is good, it returns a Namespace object where your values are accessible like:
# args.num1, args.num2, args.operation


print(args)
try:
    if(args.operation == "add"):
        print(f"The addition of num1 and num2 is {args.num1+ args.num2}")
    elif(args.operation == "sub"):
        print(f"The subtraction of num1 and num2 is {args.num1 - args.num2}")
    elif(args.operation == "mul"):
        print(f"The multiplication  of num1 and num2 is {args.num1 * args.num2}")
    elif(args.operation == "div"):
        print(f"The divsion of num1 and num2 is {args.num1 / args.num2}")
    else:
        print("Unknown Error Occurred!")
except ZeroDivisionError:
    print("Division By Zero is not Possible!")
