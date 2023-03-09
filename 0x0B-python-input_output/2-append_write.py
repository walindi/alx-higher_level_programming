#!/usr/bin/python3
"""Defines a function that appends str to text file"""


def append_write(filename="", text=""):
    """Appends a str at the end of a text file (UTF8)

    Args:
        filename (str): name of the file to which str is appended
        text (str): the string to append to file

    Return:
        the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    return len(text)
