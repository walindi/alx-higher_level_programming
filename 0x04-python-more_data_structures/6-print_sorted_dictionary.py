#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dict by ordered keys"""

    for k in sorted(a_dictionary):
        print(f"{k}: {a_dictionary[k]}")
