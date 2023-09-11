#!/usr/bin/python3
"""
Module contains a funtion
that adds an attribute to a class
if it can
"""


def add_attribute(a_class, attribute, value):
    """
    a function that adds a new attribute to an object if it’s possible:
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, attribute, value)
