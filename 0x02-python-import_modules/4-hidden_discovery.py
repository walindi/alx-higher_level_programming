#!/usr/bin/python3

"""Print all names defined in compiled hidden4 module downloaded locally"""


def printNames():
    names = dir(hidden_4)
    for name in names:
        if name[0:2] != "__":
            print(name)


if __name__ == "__main__":
    import hidden_4
    printNames()
