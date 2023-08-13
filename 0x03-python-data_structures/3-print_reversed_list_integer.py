#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    b = a - 1
    for i in range(b, -1, -1):
        print("{:d}".format(my_list[i]))
