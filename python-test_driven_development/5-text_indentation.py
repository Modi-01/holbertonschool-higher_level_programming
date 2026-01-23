#!/usr/bin/python3
"""
This module defines the function text_indentation.

The text_indentation function prints a text with 2 new lines after each
of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    chunk = ""
    for ch in text:
        if ch in ".?:":
            print(chunk.strip(" "), end="")
            print(ch)
            print()
            chunk = ""
        else:
            chunk += ch

    print(chunk.strip(" "), end="")
