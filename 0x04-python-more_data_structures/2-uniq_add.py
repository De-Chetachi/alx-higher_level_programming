#!/usr/bin/python3
'''
a function that adds all unique integers in a list (only once for each integer)
'''


def uniq_add(my_list=[]):
    sum_ = 0
    for a in set(my_list):
        sum_ = sum_ + a
    return (sum_)
