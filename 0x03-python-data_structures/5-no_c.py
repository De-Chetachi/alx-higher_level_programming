#!/usr/bin/python
def no_c(my_string):
    new_str = ""
    if my_string:
        for c in my_string:
            if ord('c') != ord(c) and ord('C') != ord(c):
                new_str += c
    return (new_str)

