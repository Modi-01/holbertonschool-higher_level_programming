#!/usr/bin/python3
"""
This module contains the function text_indentation.

The text_indentation function prints a text with 2 new lines after each
of these characters: '.', '?' , ':' and '!' and ensures no space at the
beginning or at the end of each printed line.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?', ':', and '!'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:!"
    chunk = ""

    for ch in text:
        chunk += ch
        if ch in delimiters:
            print(chunk.strip(), end="\n\n")
            chunk = ""

    if chunk:
        print(chunk.strip(), end="")
