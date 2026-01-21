#!/usr/bin/python3
"""
5-no_c
"""


def no_c(my_string):
    """Return a new string with all 'c' and 'C' characters removed."""
    new_str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
