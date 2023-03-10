#!/usr/bin/python3
"""Defines a file reading function"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
