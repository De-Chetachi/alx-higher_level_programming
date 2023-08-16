#!/usr/bin/python3
'''
a function that returns a new dictionary with all values multiplied by 2
'''


def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        a_dictionary[i] = a_dictionary[i] * 2
    return (a_dictionary)
