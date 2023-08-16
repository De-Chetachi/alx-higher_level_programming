#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix_ = []
        for i in matrix:
            a = [x ** 2 for x in i]
            matrix_.append(a)
        return(matrix_)
