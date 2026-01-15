#!/usr/bin/python3


def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""

    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            result += chr(ord(ch) - 32)
        else:
            result += ch

    print("{}".format(result))
