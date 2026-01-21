#!/usr/bin/python3
"""
Module: 4-only_diff_elements
Contains a function that returns a set of all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):
    """
    Return a set of elements that are present in only one of the two sets.

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: symmetric difference of set_1 and set_2
    """
    return set_1 ^ set_2
