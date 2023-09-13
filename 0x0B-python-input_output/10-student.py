#!/usr/bin/python3
'''json module'''


class Student:
    ''' class Student that defines a student by:'''

    def __init__(self, first_name, last_name, age):
        '''Instantiation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''a oublic method  that retrieves a dictionary
        representation of a Student instance'''
        if type(attrs) is not list:
            return (self.__dict__)

        new = True
        for element in attrs:
            if type(element) != str:
                new = False
        if new:
            dict_ = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dict_[attr] = self.__dict__[attr]
            return (dict_)
        else:
            return (self.__dict__)
