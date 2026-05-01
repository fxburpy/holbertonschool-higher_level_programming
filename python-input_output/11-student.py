#!/usr/bin/python3
"""
Module that defines a Student class with serialization
and deserialization capabilities.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using key-value pairs from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
