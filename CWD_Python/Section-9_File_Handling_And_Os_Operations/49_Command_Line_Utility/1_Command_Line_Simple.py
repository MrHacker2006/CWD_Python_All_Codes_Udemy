import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", type=int, help="desciption of argument1")
parser.add_argument("num2", type=int, help="desciption of argument2")

args = parser.parse_args()

print(args.num1)
print(args.num2)

# python 1_Command_Line_Simple.py 5 6
# python 1_Command_Line_Simple.py --help