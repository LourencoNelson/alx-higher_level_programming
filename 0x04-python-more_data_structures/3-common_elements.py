#!/usr/bin/python3

def common_elements(set_1, set_2):
    result = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                result.add(j)
                break
    return result
