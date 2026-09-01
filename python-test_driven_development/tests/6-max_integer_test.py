#!/usr/bin/python3
"""Unit tests for the ``max_integer`` function."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Verify maximum selection across common list shapes."""

    def test_ordered_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_integers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_maximum_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-4, -2, -9]), -2)

    def test_single_value(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_repeated_maximum(self):
        self.assertEqual(max_integer([5, 1, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 4.2, 3.8]), 4.2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, 7.5, -3, 7]), 7.5)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "pear", "banana"]), "pear")


if __name__ == "__main__":
    unittest.main()
