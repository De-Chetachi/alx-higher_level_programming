#!/usr/bin/python3
'''
 a function that returns the weighted average of
 all integers tuple (<score>, <weight>)
'''


def weight_average(my_list=[]):
    avg = 0
    if my_list:
        num = 0
        dino = 0
        for i, j in my_list:
            num = num + (i * j)
            dino = dino + j
        avg = num / dino
    return (avg)
