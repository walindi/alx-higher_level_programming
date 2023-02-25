#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggerst int value"""

    if a_dictionary:
        sortedDict = sorted(a_dictionary.items())
        # sortedDict is a list of a_dictionary k/v pairs in ascending order
        # k/v pairs in the list are tuples

        return sortedDict[-1][1]
