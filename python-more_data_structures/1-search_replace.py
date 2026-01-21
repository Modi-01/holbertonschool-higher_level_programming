#!/usr/bin/python3
"""
Module: 1-search_replace
Contains a function that replaces all occurrences of an element in a list
by another element in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replace all occurrences of `search` in `my_list` by `replace`.

    Args:
        my_list (list): original list
        search: element to replace
        replace: new element

    Returns:
        list: a new list with replacements applied
    """
    return [replace if item == search else item for item in my_list]
