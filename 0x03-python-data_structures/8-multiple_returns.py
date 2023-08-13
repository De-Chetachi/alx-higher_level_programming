#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if sentence and a > 0:
        b = sentence[0]
    else:
        b = "None"
    c = a, b
    return (c)
