#!/usr/bin/python3
"""Define a square based on the full rectangle implementation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a private size."""

    def __init__(self, size):
        """Initialize a square after validating its size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square area."""
        return self.__size ** 2
