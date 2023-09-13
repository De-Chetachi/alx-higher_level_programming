#!/usr/bin/python3
'''json module'''


def class_to_json(obj):
    ''' a function that returns the dictionary description with simple data'''
    return (obj.__dict__)
