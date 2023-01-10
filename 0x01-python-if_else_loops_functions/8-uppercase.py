#!/usr/bin/python3

def uppercase(str):
    for s in str:
        exp = ord(s) in range(97, 123)
        print("{}".format(chr(ord(s)-32) if exp else s), end="")
    print()
