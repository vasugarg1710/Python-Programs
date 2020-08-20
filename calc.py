# Faulty calculator
import argparse
import sys


def calc(args):
    if args.o == "+":
        if args.a == 56 and args.b == 9:
            return 77
        else:
            return args.a + args.b
    elif args.o == "-":
        return args.a - args.b
    elif args.o == "*":
        if args.a == 45 and args.b == 3:
            return 555
        else:
            return args.a * args.b
    elif args.o == "/":
        if args.a == 56 and args.b == 6:
            return 4
        else:
            return args.a / args.b
    else:
        return"Invalid input"


parser = argparse.ArgumentParser(description='This program is a calculator')
parser.add_argument('--o', default='+', help='Enter the operator')
parser.add_argument('--a', default='1', type=int, help='Enter the first number')
parser.add_argument('--b', default='1', type=int, help='Enter the second number')

args = parser.parse_args()
sys.stdout.write(str(calc(args)))
