#!/usr/bin/python3

if __name__ == "__main__":
    def lookup(obj):
        """Returns a list of all avaliable attributes and methods of an obj"""
        return list(dir(obj))
