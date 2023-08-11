#!/usr/bin/python3
from sys import exit
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    size = len(argv)
    ac = size - 1
    if ac == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            res = add(a, b)
        elif argv[2] == "-":
            res = sub(a, b)
        elif argv[2] == "*":
            res = mul(a, b)
        elif argv[2] == "/":
            res = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{:d} {} {:d} {} {:d}".format(a, argv[2], b, "=", res))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
