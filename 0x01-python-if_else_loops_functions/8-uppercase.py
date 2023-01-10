#!/usr/bin/python3

def uppercase(str):
    for s in str:
        print("{}".format(chr(ord(s)-32) if s.islower else s), end="")
    print()
