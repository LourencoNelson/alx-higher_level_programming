#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of arguments"""
    from sys import argv
    size = len(argv) - 1

    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, argv[i]))
