#!/usr/bin/python3
"""Module to find the maximum integer in a list."""


def max_integer(list=[]):
    """Return the maximum value in a list, or ``None`` when it is empty."""
    if len(list) == 0:
        return None
    result = list[0]
    index = 1
    while index < len(list):
        if list[index] > result:
            result = list[index]
        index += 1
    return result
