#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dict with all values multiplied by 2"""

    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
