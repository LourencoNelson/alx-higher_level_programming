#!/usr/bin/python3

if __name__ == "__main__":
    """Print basic math operations with 10 and 5."""
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
