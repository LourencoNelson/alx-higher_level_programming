#!/usr/bin/python3

def uniq_add(my_list=[]):
    # uniq = []
    # uniq = [i for i in my_list if i not in uniq]
    return sum(set(my_list))
