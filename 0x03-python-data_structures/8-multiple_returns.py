#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        if (a > 0):
            b = sentence[0]
    else:
        b = "None"
    c = a, b
    return (c)
