#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    res = 0
    try:
        for i in range(0,x):
            print("{}".format(my_list[i]), end="")
            res += 1
    except:
        pass
    print()
    return (res)
