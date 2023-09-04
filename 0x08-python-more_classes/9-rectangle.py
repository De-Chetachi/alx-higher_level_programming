#!/usr/bin/python3
'''this module contains a rectangle class'''


class Rectangle:
    '''class Rectangle that defines a rectangle by'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''gets the width property'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''sets width property'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets the height property'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height property'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        a = self.__width * 2
        b = self.__height * 2
        return (a + b)

    def __str__(self):
        '''defines a private instsance str method'''
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + str(self.print_symbol)
            if i != self.__height - 1:
                rec = rec + "\n"
        return (rec)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        if rect_2.area() > rect_1.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''Class method returns a new Rectangle instance'''
        u = Rectangle(size, size)
        return (u)

    def __repr__(self):
        '''defines a private instsance repr method'''

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
