#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds 2 integers
    Arguments of type float are casted into int

    Args must be int or float otherwise a TypeError is raised
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
