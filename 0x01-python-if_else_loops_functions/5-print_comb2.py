#!/usr/bin/python3
for my_i in range(100):
    if my_i != 99:
        print("{my_num:02d}, ".format(my_num=my_i), end="")
    else:
        print("{my_num:02d}\n".format(my_num=my_i), end="")
