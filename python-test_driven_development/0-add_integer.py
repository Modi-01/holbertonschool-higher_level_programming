#!/usr/bin/python3
"""Module that provides a function to add two numbers."""


def add_integer(a, b=98):
    """Return the addition of a and b as an integer."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) is float:
        if a != a or a in (float("inf"), float("-inf")):
            raise TypeError("a must be an integer")
    if type(b) is float:
        if b != b or b in (float("inf"), float("-inf")):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
