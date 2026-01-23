#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)


if __name__ == "__main__":
    unittest.main()
