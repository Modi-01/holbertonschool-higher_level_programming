#!/usr/bin/python3
"""
Module: 10-best_score
Return the key with the biggest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """
    Return a key with the biggest integer value.

    If a_dictionary is None or empty, return None.

    Args:
        a_dictionary (dict): dictionary of scores (int values)

    Returns:
        str or None: key with highest value, or None if not found
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key

    return best_key
