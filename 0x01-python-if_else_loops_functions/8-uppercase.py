#!/usr/bin/python3

def uppercase(str):
    for s in str:
        print("{}".format(chr(ord(s)-32) if (ord(s) in range(97, 123)) else s), end="")
    print()
