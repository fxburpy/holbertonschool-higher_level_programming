#!/usr/bin/python3
"""This module defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
