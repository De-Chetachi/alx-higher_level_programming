#!/usr/bin/python3
"""
this module contains
a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    a class Rectangle that inherits
    from BaseGeometry
    '''

    def __init__(self, width, height):
        '''initializes a  rectangle object'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''an area method'''
        return (self.__height * self.__width)

    def __str__(self):
        '''defines a private instsance str method'''
        rec = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return (rec)
