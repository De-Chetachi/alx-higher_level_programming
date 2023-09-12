#!/usr/bin/python3
'''file input and output module'''


def read_file(filename=""):
    ''' function that reads a text file (UTF8) and prints it to stdout:'''
    with open(filename, 'r', encoding="utf-8") as file_:
        for line in file_:
            print(line, end='')
