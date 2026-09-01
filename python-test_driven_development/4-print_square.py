#!/usr/bin/python3
"""Provide a function that prints a square using hash characters."""


def print_square(size):
    """Print a square with sides of length ``size``."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
