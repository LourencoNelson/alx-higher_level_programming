#!/usr/bin/python3

def weight_average(my_list=[]):
    num = denum = 0

    if not my_list:
        return 0

    for item in my_list:
        num += item[0]*item[1]
        denum += item[1]
    return num/denum
