#!/usr/bin/python3

def islower(c):
    if ord(c) in range(97, 123):
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
