#!/usr/bin/python3
'''list subclass'''


class MyList(list):
    '''a subclass of list'''

    def print_sorted(self):
        '''prints a sorted list'''

        _list = super().copy()
        _list.sort()
        print(_list)
