#!/usr/bin/python3
"""
0-print_list_integer
"""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for num in my_list:
        print("{:d}".format(num))
