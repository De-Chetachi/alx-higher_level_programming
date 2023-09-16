#!/usr/bin/python3
'''base module'''
from json import dumps
from json import loads
from os.path import isfile


class Base:
    '''This class will be the “base” of all other classes in this project.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if type(list_dictionaries) is None or len(list_dictionaries) == 0:
            return (dumps([]))
        return (dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs
        to a file:'''
        if list_objs is not None:
            save = []
            for obj in list_objs:
                x = obj.to_dictionary()
                save.append(x)
        else:
            save = []
        save = Base.to_json_string(save)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as file_:
            file_.write(save)


    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return ([])
        return (loads(json_string))


    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1,1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
            return (dummy)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances:'''
        obj_created = []
        filename = "{}.json".format(cls.__name__)
        if isfile(filename):
            with open(filename, 'r', encoding="utf-8") as file_:
                line = file_.readline()
            list_ = Base.from_json_string(line)
            for list_e in list_:
                obj_create = cls.create(**list_e)
                obj_created.append(obj_create)

        return (obj_created)

