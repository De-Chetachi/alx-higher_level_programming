#!/usr/bin/python3
'''rectangle module'''
from models.base import Base

class Rectangle(Base):
    '''Class Rectangle inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class constructor'''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        '''returns the area value of the Rectangle instance'''
        return (self.__width * self.__height)


    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        rec = ""
        rec = rec + ("\n" * self.y)
        for i in range(self.__height):
            rec = rec + (" " * self.x)
            rec = rec + ("#" * self.__width + '\n')
        print(rec, end="")


    def __str__(self):
        '''private instance method'''
        rec = "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
        return (rec.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''public method  assigns an argument to each attribute'''
        if (type(args) is not None) and (len(args) > 0):
            try:
                self.id = args[0]
            except IndexError:
                return(0)
            try:
                self.__width = args[1]
            except IndexError:
                return (0)
            try:
                self.__height = args[2]
            except IndexError:
                return (0)
            try:
                self.__x = args[3]
            except IndexError:
                return (0)
            try:
                self.__y = args[4]
            except IndexError:
                return (0)

        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)


    def to_dictionary(self):
        dict_ = {}
        list_ = ["id", "width", "height", "x", "y"]
        for key in list_:
                dict_[key] = self.__getattribute__(key)
        return (dict_)
