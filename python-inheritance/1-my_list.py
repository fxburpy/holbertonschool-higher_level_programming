#!/usr/bin/python3
"""This module defines a MyList class."""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
