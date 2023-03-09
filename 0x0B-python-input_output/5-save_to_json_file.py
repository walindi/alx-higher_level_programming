#!/usr/bin/python3
"""Defines a function that serializes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a json representation
    Args:
        my_obj (): the object to be serialized
        filename (str): the name of the text file
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
