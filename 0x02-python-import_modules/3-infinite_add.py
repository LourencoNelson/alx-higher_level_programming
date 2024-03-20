#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the sum of all arguments"""
    from sys import argv
    size = len(argv) - 1
    s = 0
    for i in range(1, size + 1):
        s += int(argv[i])
    else:
        print("{}".format(s))
