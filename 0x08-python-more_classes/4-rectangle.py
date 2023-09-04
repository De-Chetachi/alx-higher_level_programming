#!/usr/bin/python3
'''this module contains a rectangle class'''


class Rectangle:
    '''class Rectangle that defines a rectangle by'''
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''gets the width property'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''sets width property'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets the height property'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height property'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        a = self.__width * 2
        b = self.__height * 2
        return (a + b)

    def __str__(self):
        '''defines a private instsance str method'''
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + "#"
            if i != self.__height - 1:
                rec = rec + "\n"
        return (rec)

    def __repr__(self):
        '''defines a private instsance repr method'''
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
