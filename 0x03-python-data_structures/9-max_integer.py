#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list"""

    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
