#!/usr/bin/python3
"""Serialize and deserialize custom objects with pickle."""

import pickle


class CustomObject:
    """Represent a person that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this object to ``filename`` or return ``None`` on error."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an object, or ``None`` on error."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
