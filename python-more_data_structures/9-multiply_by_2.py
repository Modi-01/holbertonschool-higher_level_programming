#!/usr/bin/python3
"""
Module: 9-multiply_by_2
Return a new dictionary where all values are multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): dictionary with integer values

    Returns:
        dict: new dictionary with values multiplied by 2
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
