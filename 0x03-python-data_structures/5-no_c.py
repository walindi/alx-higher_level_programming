#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string

    Args:
        my_string (str): the string to be checked
    """

    new_string = ""

    for char in my_string:
        if char != "c" and char != "C":
            new_string += char

    return new_string
