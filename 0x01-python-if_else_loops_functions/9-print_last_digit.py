#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        n = -number
    else:
        n = number
    print("{}".format(n % 10), end="")
    return n % 10
