#!/usr/bin/python3
"""Define a list subclass with sorted printing support."""


class MyList(list):
    """Extend ``list`` with a non-mutating sorted print method."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
