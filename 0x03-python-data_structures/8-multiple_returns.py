#!/usr/bin/python3

def multiple_returns(sentence):
    """Return tuple with the length of a string and its 1st character

    Args:
        sentence: the string to be checked
    """

    tup = len(sentence), sentence[0]

    return tup
