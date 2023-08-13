#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        a = len(my_list)
        if idx < 0:
            return (my_list)
        elif idx >= a:
            return (my_list)
        else:
            new_list = []
            for i in range (a):
                if i == idx:
                    new_list.append(element)
                else:
                    new_list.append(my_list[i])
            return (new_list)
