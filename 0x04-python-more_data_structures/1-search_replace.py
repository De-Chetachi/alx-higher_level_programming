#!/usr/bin/python3

'''
a function that replaces all occurrences of an element by another
in a new list.
my_list is the initial list
search is the element to replace in the list
replace is the new element
'''


def search_replace(my_list, search, replace):
    if my_list:
        my_list_ = [replace if ele == search else ele for ele in my_list]
        return (my_list_)
