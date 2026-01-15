#!/usr/bin/python3


def islower(c):
    """Check if a character is lowercase.

    Args:
        c: Character to check.

    Returns:
        True if c is lowercase, otherwise False.
    """
    return ord('a') <= ord(c) <= ord('z')
