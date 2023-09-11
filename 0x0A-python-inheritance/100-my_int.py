#!/usr/bin/python3
"""
Module contains a myint class
"""


class MyInt(int):
    '''myint class'''

    def __eq__(self, element):
        '''not equal'''
        return (self.real != element)

    def __ne__(self, element):
        '''equal'''
        return (self.real == element)
