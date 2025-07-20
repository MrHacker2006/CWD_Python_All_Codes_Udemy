import argparse

parser = argparse.ArgumentParser()

parser.add_argument("positional", help="description of positional argument")

args = parser.parse_args()

print(args.positional)

# python 3_Command_Line_Positional_Argument.py --help

# python 3_Command_Line_Positional_Argument.py (any sentence)/(any string)
