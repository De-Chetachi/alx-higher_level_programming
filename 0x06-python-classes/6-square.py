#!/usr/bin/python3


'''in this module contains a class that defines a square'''


class Square:
    '''this class defines a class square'''

    def __init__(self, size=0, position=(0, 0)):
        '''initializes an instance of class sqquare'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or (len(position) != 2) or not
                isinstance(position[0], int) or not
                isinstance(position[1], int)
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        '''retrives the set property position'''

        return (self.__position)

    @position.setter
    def position(self, value):
        '''position property setter'''

        if (not isinstance(value, tuple) or len(value != 2) or not
                isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
