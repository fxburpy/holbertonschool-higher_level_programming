#!/usr/bin/python3
"""
Module that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes.
    """
    return obj.__dict__
