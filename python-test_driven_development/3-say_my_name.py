#!/usr/bin/python3
"""Module that defines a function to print a formatted full name."""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name = "{} {}".format(first_name, last_name)
    print("My name is {}".format(full_name))
