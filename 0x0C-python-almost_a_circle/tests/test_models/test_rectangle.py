#!/usr/bin/python3
'''this module contains test for '''


import unittest
from models.base import Base
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    '''this class contains test cases for class rectangle'''
    def setUp(self):
        '''resets id'''
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        '''tests rectangle constructor'''
        #Base._Base__nb_objects = 0
        rec_1 = Rectangle(1, 2)
        self.assertEqual(rec_1.width, 1)
        self.assertEqual(rec_1.height, 2)
        self.assertEqual(rec_1.id, 1)


        rec_2 = Rectangle(10, 2, id = 10)
        self.assertEqual(rec_2.width, 10)
        self.assertEqual(rec_2.height, 2)
        self.assertEqual(rec_2.id, 10)

        rec_3 = Rectangle(2, 10)
        self.assertEqual(rec_3.id, 2)
        self.assertEqual(rec_3.width, 2)
        self.assertEqual(rec_3.height, 10)


        rec_4 = Rectangle(1, 2)
        self.assertEqual(rec_4.width, 1)
        self.assertEqual(rec_4.height, 2)
        self.assertEqual(rec_4.id, 3)


        with self.assertRaises(TypeError):
            Rectangle("5", 3)

        with self.assertRaises(TypeError):
            Rectangle(5, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-5, 3)

        with self.assertRaises(ValueError):
            Rectangle(5, -3)

        with self.assertRaises(ValueError):
            Rectangle(0, -2)

        with self.assertRaises(ValueError):
            Rectangle(3, 0)

        with self.assertRaises(ValueError):
            Rectangle(3, 5, -7)

        with self.assertRaises(ValueError):
            Rectangle(3, 5, 7, -9)

        self.assertEqual(Rectangle(3, 5).area(), 15)


        self.assertEqual(Rectangle(2, 3, 5, 7, 9).__str__(), '[Rectangle] (9) 5/7 - 2/3')

    if __name__ == '__main__':
        unittest.main()
