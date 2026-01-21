#!/usr/bin/python3
"""
Module: 8-simple_delete
Contains a function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary.

    If the key doesn't exist, the dictionary is not modified.

    Args:
        a_dictionary (dict): dictionary to update
        key (str): key to delete

    Returns:
        dict: the updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
