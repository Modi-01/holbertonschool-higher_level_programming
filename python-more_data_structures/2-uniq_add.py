#!/usr/bin/python3
"""
Module: 2-uniq_add
Contains a function that adds all unique integers in a list.
"""


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (each integer only once).

    Args:
        my_list (list): list of integers

    Returns:
        int: sum of unique integers
    """
    total = 0
    seen = []

    for num in my_list:
        if num not in seen:
            seen.append(num)
            total += num

    return total
