#!/usr/bin/python3

for i in range(26, 0, -1):
    if i % 2 == 0:
        print("{}".format(chr(ord('a') + i - 1)), end="")
    else:
        print("{}".format(chr(ord('A') + i - 1)), end="")
