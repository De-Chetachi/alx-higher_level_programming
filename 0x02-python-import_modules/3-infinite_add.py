#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    sum_ = 0
    for i in range(1, size):
        sum_ += int(argv[i])
    print("{:d}".format(sum_))
