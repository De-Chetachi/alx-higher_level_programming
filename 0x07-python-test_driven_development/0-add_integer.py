#!/usr/bin/python3
''''this module contains a function that adds two integers'''

def add_integer(a, b=98):
    '''
    this function adds two integer or float parameters
    
    Args:
        a: float or integer
        b: an integer or number(default 98)


    Raises:
        typeError: if not float or integer


    Returns:
        int
    '''

    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
        else:
            a = int(a)
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    return(a + b)
