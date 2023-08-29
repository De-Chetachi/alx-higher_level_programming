#!/usr/bin/python3


'''in this module contains a class that defines a square'''


class Square:
    '''this class defines a class square'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
