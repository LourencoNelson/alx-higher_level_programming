#!/usr/bin/python3

def uppercase(str):
    for s in str:
        if s.islower():
            print("{}".format(char(ord(s)-32)), end="")
        else:
            print("{}".format(s), end="")
    print()
