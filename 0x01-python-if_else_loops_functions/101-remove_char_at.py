#!/usr/bin/python3

def remove_char_at(str, n):
    """
    create a copy of the string,
    removing the character at the position n

    Args:
        str: the string to be manipulated
        n: position in the string
    """

    if n >= 0:
        return str[:n] + str[(n + 1):]
    else:
        return str
