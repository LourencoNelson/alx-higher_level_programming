#!/usr/bin/python3

num = 0
for num in range(100):
    if (num == 99):
        print("{}\n".format(num))
    else:
        print("{}, ".format(num), end="")
