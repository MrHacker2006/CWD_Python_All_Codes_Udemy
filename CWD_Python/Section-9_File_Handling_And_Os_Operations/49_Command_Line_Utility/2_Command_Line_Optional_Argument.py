import argparse

parser = argparse.ArgumentParser()

#"I want to add an optional argument that users can pass either with a short flag -o or a long flag --optional."
parser.add_argument("-o", "--optional", help="description of optional argument")

args = parser.parse_args()

print(args.optional)

# python 2_Command_Line_Optional_Argument.py --help

# python 2_Command_Line_Optional_Argument.py -o (any sentence)/(any integer)
# python 2_Command_Line_Optional_Argument.py --optional (any sentence)/(any integer)
#  python 2_Command_Line_Optional_Argument.py  # None will be the output