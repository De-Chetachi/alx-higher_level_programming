#!/usr/bin/python3
'''json module'''
from sys import argv
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


size = len(argv)
if path.isfile("add_item.json"):
    list_ = load_from_json_file("add_item.json")
else:
    list_ = []
for i in range(1, size):
    list_.append(argv(i))
save_to_json_file(list_, "add_item.json")
