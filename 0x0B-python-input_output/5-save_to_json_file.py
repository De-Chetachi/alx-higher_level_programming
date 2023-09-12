#!/usr/bin/python3
'''json module'''
from json import load
from json import dumps


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file,
    using a JSON representation:'''
    with open(filename, 'w', encoding="utf-8") as file_:
        x = dumps(my_obj)
        file_.write(x)
