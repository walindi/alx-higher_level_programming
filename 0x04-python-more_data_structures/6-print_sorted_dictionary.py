#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dict by ordered keys"""

    for k,v in sorted(a_dictionary.items()):
        print(f"{k}: {v}")
