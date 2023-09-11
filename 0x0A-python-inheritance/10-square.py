#!/usr/bin/python3
"""
Module contains a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''a class Square that inherits from Rectangle (9-rectangle.py)'''
    def __init__(self, size):
        '''ínstantiation'''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''method calculates the area of square class'''
        return (super().area())
