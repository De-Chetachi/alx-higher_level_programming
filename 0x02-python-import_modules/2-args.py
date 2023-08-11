#!/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    if size == 1:
        str_ = "arguments."
    elif size == 2:
        str_ = "argument:"
    elif size > 2:
        str_ = "arguments:"

    print("{:d} {}".format(size - 1, str_))
    if size > 0:
        for i in range(1, size):
            print("{:d}: {}".format(i, argv[i]))
