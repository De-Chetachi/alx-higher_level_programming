#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        if (a <= 0):
            b = "None"
        else:
            b = sentence[0]
        c = a, b
        return (c)
