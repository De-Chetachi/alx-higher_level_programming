#!/usr/bin/python3
'''
a function that computes the square value of all integers of a matrix
'''


def square(n):
    return (n ** 2)


def square_matrix_simple(matrix=[]):
    if matrix:
        matrix_ = [list(map(square, mat)) for mat in matrix]
        return (matrix_)
