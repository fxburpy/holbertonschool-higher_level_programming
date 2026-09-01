#!/usr/bin/python3
"""Provide exact class identity checking."""


def is_same_class(obj, a_class):
    """Return ``True`` only when ``obj`` is exactly an ``a_class`` instance."""
    return type(obj) is a_class
