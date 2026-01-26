#!/usr/bin/python3
"""Defines a Square class that can compute its area."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize a Square instance and validate the size value."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
