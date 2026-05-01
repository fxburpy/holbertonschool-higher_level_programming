#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
