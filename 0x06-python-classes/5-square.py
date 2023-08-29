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

    @property
    def size(self):
        '''retrives the set property size'''

        return (self.__size)

    @size.setter
    def size(self, value):
        '''size property setter'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''defines an instance method area
        which is a function that calculates the
        area of the an instance of the square'''

        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
