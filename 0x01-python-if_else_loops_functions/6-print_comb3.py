#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if num1 == 8 and num2 == 9:
            print("{a}{b}\n".format(a=num1, b=num2), end="")
        elif num1 < num2 and num1 != num2:
            print("{a}{b}, ".format(a=num1, b=num2), end="")
