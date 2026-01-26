#!/usr/bin/python3
"""Defines a Square class with validated size property and area method."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square instance with a validated size value."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating its type and value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
