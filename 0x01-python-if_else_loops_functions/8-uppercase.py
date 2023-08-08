#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - hex(19))
            print("{character}".forma(character=char), end="")
