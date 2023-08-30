#!/usr/bin/python3

import math
''''this module defines a magic class'''


class MagicClass:
    '''this class defines a magic class:)'''

    def __init__(self, radius=0):
        '''the initializer'''

        self.__radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''defines the radius of the class'''

        return((self.__radius ** 2) * math.pi)

    def circumference(self):
        '''defines the circumference of the class'''

        return((2 * math.pi) * self.__radius)
