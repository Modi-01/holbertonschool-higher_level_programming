#!/usr/bin/python3
"""
Module: 6-print_sorted_dictionary
Contains a function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys (alphabetical order).

    Only the first level keys are sorted. Values can be any type.

    Args:
        a_dictionary (dict): dictionary to print
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
