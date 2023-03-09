#!/usr/bin/python3
"""Module 6-load_from_json_file
Defines a function that deserializes json file"""

import json


def load_from_json_file(filename):
    """Creates an object from a "json file"""

    with open(filename, 'r') as f:
        json.load(f)
