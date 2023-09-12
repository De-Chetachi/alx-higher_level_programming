#!/usr/bin/python3
'''json module'''
from json import load
from json import dumps


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file,
    using a JSON representation:'''
    x = dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as file_:
        file_.write(x)
