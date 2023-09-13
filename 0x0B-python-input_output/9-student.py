#!/usr/bin/python3
'''json module'''


class Student:
    ''' class Student that defines a student by:'''

    def __init__(self, first_name, last_name, age):
        '''Instantiation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''a oublic method  that retrieves a dictionary
        representation of a Student instance'''
        return (self.__dict__)
