#!/usr/bin/python3
'''json module'''
from json import load


def from_json_string(my_str):
    '''function that returns the JSON representation of an object (string)'''
    with open("json.txt", 'w', encoding="utf-8") as file_:
        file_.write(my_str)
    with open("json.txt", 'r', encoding="utf-8") as file__:
        return (load(file__))
