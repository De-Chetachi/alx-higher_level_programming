#!/usr/bin/python3
'''square module'''
Rectangle = __import__('models.rectangle').rectangle.Rectangle


class Square(Rectangle):
    '''a square class inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor method'''
        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size


    def __str__(self):
        '''private instance method'''
        rec = "[Square] ({}) {:d}/{:d} - {:d}"
        return (rec.format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        '''size getter'''
        return (self.__size)
    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value


    def update(self, *args, **kwargs):
        '''public method  assigns an argument to each attribute'''
        if (type(args) is not None) and (len(args) > 0):
            try:
                self.id = args[0]
            except IndexError:
                return(0)
            try:
                self.width = args[1]
            except IndexError:
                return (0)
            try:
                self.height = args[1]
            except IndexError:
                return (0)
            try:
                self.__size = args[1]
            except IndexError:
                return (0)
            try:
                self.x = args[2]
            except IndexError:
                return (0)
            try:
                self.y = args[3]
            except IndexError:
                return (0)

        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)


    def to_dictionary(self):
        dict_ = {}
        list_ = ["id", "size", "x", "y"]
        for key in list_:
                dict_[key] = self.__getattribute__(key)
        return (dict_)
