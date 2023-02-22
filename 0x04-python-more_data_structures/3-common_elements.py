#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Return a set of common elements in two sets"""
    common = [item for item in set_1 if item in set_2]
    return common
