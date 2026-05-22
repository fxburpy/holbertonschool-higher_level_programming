#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry')

class Rectangle(BaseGeometry.BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
