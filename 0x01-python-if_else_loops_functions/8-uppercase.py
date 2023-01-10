#!/usr/bin/python3

def uppercase(str):
    for s in str:
        print("{}".format(if s.islower: chr(ord(s)-32)) else: s, end="")
    print()
