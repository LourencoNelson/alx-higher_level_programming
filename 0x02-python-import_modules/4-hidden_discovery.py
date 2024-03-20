#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all names defined by the module hidden_4.pyc"""
    import hidden_4

    li = list(dir(hidden_4))
    for n in li:
        if n[:2] != "__":
            print("{}".format(n))
