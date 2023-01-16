#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list, only once for each"""

    total = 0

    for integer in set(my_list):
        total += integer

    return total
