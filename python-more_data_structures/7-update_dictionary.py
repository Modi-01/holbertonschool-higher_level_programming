#!/usr/bin/python3
"""
Module: 7-update_dictionary
Contains a function that replaces or adds a key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    If the key exists, its value is replaced.
    If the key doesn't exist, it is created.

    Args:
        a_dictionary (dict): dictionary to update
        key (str): key to update/add
        value: value to set (any type)

    Returns:
        dict: the updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
