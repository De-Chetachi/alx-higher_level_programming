#!/usr/bin/python3
'''base module'''
from json import dumps
from json import loads
import csv
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
            dummy = cls(1, 1)
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

    """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes'in csv'''
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w') as file_:
            writer = csv.writer(file_, delimiter=',', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
            for obj in list_objs:
                obj_ = obj.to_dictionary()
                writer.writerow(obj_)

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes'in csv'''
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        if isfile(filename):
            list_ = []
            with open(filename, 'r') as file_:
                reader = csv.reader(file_, delimiter=',')
                for line in reader:
                    list_.append(line)
                    if type(line) is dict:
                        dicty = list_attr
                    elif type(line) is list:
                        dicty = cls.to_dict(line)
                    list_.append(dicty)
            for list_attr in list_:
                create_ = cls.create(**dicty)
                list_objs.append(create_)
        return (list_objs)


    @classmethod
    def to_list(cls, obj):
        list of object attributes
        attr_list = []
        dict_ = obj.to_dictionary()
        for key, value in dict_.items():
            attr_list.append(dict_[key])
        return(attr_list)


    @classmethod
    def to_dict(cls, list_attrs):
        dict_ = {}
        list_ = ["id", "width", "height", "x", "y"]
        list_s = ["id", "size", "x", "y"]
        dict_['id'] = list_attrs[0]

        i = 1
        if cls.__name__ == "Rectangle":
            for key in list_:
                try:
                    dict_[key] = list_attrs[i]
                    i += 1
                except IndexError:
                    break
            return dict_
        elif cls.__name__ == "Square":
            for key in list_s:
                try:
                    dict_[key] = list_attrs[i]
                    i += 1
                except IndexError:
                    break
            return (dict_)
    """
