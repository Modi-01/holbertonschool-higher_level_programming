#!/usr/bin/python3
"""
10-divisible_by_2
"""


def divisible_by_2(my_list=[]):
    """Return a list of True/False for divisibility by 2."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
