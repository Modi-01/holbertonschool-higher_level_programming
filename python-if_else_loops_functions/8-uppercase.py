#!/usr/bin/python3


def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            print("{}".format(chr(ord(ch) - 32)), end="")
        else:
            print("{}".format(ch), end="")
    print()
