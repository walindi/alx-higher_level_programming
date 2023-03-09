#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        filename (str): name of the file to write to
        text (str): string to be written

    return: number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return len(text)
