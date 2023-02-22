#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a  dict
    Args:
        key (str): new key
        value: value of new key
    """
    if not a_dictionary.get(key):
        a_dictionary.update({key: value})

    for k, v in a_dictionary.items():
        if k != key:
            a_dictionary[k] = v
        else:
            a_dictionary[key] = value

    return a_dictionary
