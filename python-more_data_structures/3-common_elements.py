#!/usr/bin/python3
"""
Module: 3-common_elements
Contains a function that returns a set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    """
    Return a set of elements common to both set_1 and set_2.

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: set containing common elements
    """
    return set_1 & set_2
