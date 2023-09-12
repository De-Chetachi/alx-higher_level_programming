#!/usr/bin/python3
'''json module'''
from json import load
from json import dump


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file”:'''
    with open(filename, 'r', encoding="utf-8") as file_:
        x = load(file_)
        return (x)
