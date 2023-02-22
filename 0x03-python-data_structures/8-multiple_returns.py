#!/usr/bin/python3

def multiple_returns(sentence):
    """Return tuple with the length of a string and its 1st character

    Args:
        sentence: the string to be checked
    """

    if not sentence:
        return = 0, None

    else:
        return len(sentence), sentence[0]
