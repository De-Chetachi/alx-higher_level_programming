#!/usr/bin/python3


'''in this module contains a class that defines a square'''


class Square:
    '''this class defines a class square'''

    def __init__(self, size=0):
        '''initializes an instance of class sqquare'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''defines an instance method area
        which is a function that calculates the
        area of the an instance of the square'''

        return (self.__size ** 2)
