#!/usr/bin/python3
'''base geometry module'''


class BaseGeometry:
    '''an empty class BaseGeometry'''

    def area(self):
        '''raises an Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
