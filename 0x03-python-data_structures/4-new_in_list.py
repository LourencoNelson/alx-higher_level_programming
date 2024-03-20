#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a list without modifying the list"""

    new_list = [x for x in my_list]

    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
