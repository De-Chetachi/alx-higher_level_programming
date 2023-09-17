#!/usr/bin/python3
'''this module contains test for '''


import unittest
Base = __import__('models.base').base.Base
class TestBase(unittest.TestCase):
    '''test class for class base'''
    def setUp(self):
        '''reset id to 0'''
        Base.__nb_objects = 0

    def test__init__(self):
        '''this method tests the init method of  base class'''
        base_1 = Base()
        self.assertEqual(base_1.id, 1)

        base_2 = Base()
        base_3 = Base()
        self.assertEqual(base_2.id, 2)
        self.assertEqual(base_3.id, 3)

        base_7 = Base(7)
        self.assertEqual(base_7.id, 7)

    if __name__ == '__main__':
        unittest.main()
