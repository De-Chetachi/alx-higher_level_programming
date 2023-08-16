#!/usr/bin/python3
'''
a function that returns the number of keys in a dictionary.
'''


def number_keys(a_dictionary):
    len_ = 0
    for i in a_dictionary:
        len_ = len_ + 1
    return (len_)
