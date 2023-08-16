#!/usr/bin/python3
'''
a function that deletes keys with a specific value in a dictionary
If the value doesn’t exist, the dictionary won’t change
All keys having the searched value have to be deleted
'''


def complex_delete(a_dictionary, value):
    keys = []
    for key, val in a_dictionary.items():
        if val == value:
            keys.append(key)
    for i in keys:
        del a_dictionary[i]

    return (a_dictionary)
