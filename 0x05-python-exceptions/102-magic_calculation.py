#!/usr/bin/python3
''''this module contains a magic
calculation function'''


def magic_calculation(a, b):
    '''magic calculation'''
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
        return result
