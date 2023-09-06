#!/usr/bin/python3
'''Unittest for max_integer([..]'''


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''test class'''

    def test_max_integer_empty(self):
        '''tests'''
        result = max_integer()
        self.assertIsNone(result)

    def test_max_integer_empty_list(self):
        '''tests'''
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single(self):
        '''tests'''
        result = max_integer([2])
        self.assertEqual(result, 2)

    def test_max_integer_random(self):
        '''tests'''
        result = max_integer([2, 3, 8, 6, 5 ,9])
        self.assertEqual(result, 9)

    def test_max_integer_repeat(self):
        '''tests'''
        result = max_integer([8, 8, 8])
        self.assertEqual(result, 8)

    def test_max_integer_repeat(self):
        '''tests'''
        result = max_integer([8, 6, 7])
        self.assertEqual(result, 8)

    def test_max_integer_repeat(self):
        '''tests'''
        result = max_integer([1, 2, 9, 3, 6])
        self.assertEqual(result, 9)

    def test_max_integer_repeat(self):
        '''tests'''
        result = max_integer([2, -3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_repeat(self):
        '''tests'''
        result = max_integer([-1, -2, -3])
        self.assertEqual(result, -1)

    def test_max_integer_int(self):
        '''tests'''
        with self.assertRaises(Exception):
            result = max_integer(2)

    def test_max_integer_var(self):
        '''tests'''
        with self.assertRaises(Exception):
            result = max_integer([a,b])
