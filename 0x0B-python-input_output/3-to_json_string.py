#!/usr/bin/python3
"""Defines a function that serializes object to json"""

import json


def to_json_string(my_obj):
    """returns json representation of a string object"""

    return json.dumps(my_obj)
