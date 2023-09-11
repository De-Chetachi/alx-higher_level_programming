#!/usr/bin/python3
'''this module contains a
 function that returns True if the object is exactly
 an instance of the specified class ; otherwise False.
 '''


def inherits_from(obj, a_class):
    '''
    a function that returns True if the object
    is exactly an instance of the specified class
    otherwise False.
    '''
    return (isinstance(obj, a_class) and type(obj) != a_class)
