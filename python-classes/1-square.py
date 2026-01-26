#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize a Square instance with a private size value."""
        self.__size = size
