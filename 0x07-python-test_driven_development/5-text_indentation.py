#!/usr/bin/python3
'''
module of text indentation
'''

def text_indentation(text):
    '''
     function that prints a text with
     2 new lines after each of these
     characters: ., ? and :
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")
    size = len(text)
    txt = ""
    for i in range(size):
        if text[i] in (".?:"):
            txt = (txt + text[i]).strip()
            print("{:s}\n".format(txt))
            txt = ""
        else:
            txt = txt + text[i]
    txt = txt.strip()
    print("{:s}".format(txt), end="")
