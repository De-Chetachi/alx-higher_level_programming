#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 0:
        tuple_a = 0, 0
    elif a == 1:
        tuple_a = tuple_a[0], 0
    if b == 0:
        tuple_b = 0, 0
    elif b == 1:
        tuple_b = tuple_b[0], 0

    a_ = tuple_a[0] + tuple_b[0]
    b_ = tuple_a[1] + tuple_b[1]
    new_tuple = a_, b_
    return (new_tuple)
