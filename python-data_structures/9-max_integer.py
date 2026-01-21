#!/usr/bin/python3
"""
9-max_integer
"""


def max_integer(my_list=[]):
    """Find and return the biggest integer in a list."""
    if my_list == []:
        return None

    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num
    return biggest
