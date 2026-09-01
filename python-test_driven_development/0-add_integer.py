#!/usr/bin/python3
"""Provide a function for adding two integers.

Inputs are validated and floats are converted before addition.
"""


def add_integer(a, b=98):
    """Return the integer sum of two integers or floats."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
