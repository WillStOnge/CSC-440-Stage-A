"""
MySearchTest.py
Programmer: Anthony Bosch
Course: CSC440
"""

import unittest
from MySearch import my_search


class MySearchTest(unittest.TestCase):
    """
        Test cases for my_search()
    """

    def test_search_pass(self):
        index = my_search("input.txt", 8)
        self.assertEqual(index, 6)

    def test_search_fail(self):
        index = my_search("input.txt", 0)
        self.assertEqual(index, -1)

    def test_open_file(self):
        with self.assertRaises(FileNotFoundError):
            index = my_search("my_file.txt", 8)


if __name__ == "__main__":
    unittest.main()

