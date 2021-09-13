"""
MySortTest.py

Programmer: Justin Gallagher
Course: CSC440
"""

import unittest
from MySort import my_sort


class MySortTest(unittest.TestCase):
    """
        Test cases for my_sort()
    """

    def test_givenInputFile_returnsSortedList(self):
        test_list = my_sort("input.txt")
        for index in range(len(test_list) - 1):
            self.assertLessEqual(test_list[index], test_list[index + 1],
                                 "List is not in ascending, sorted order in test:test_givenInputFile_returnsSortedList")

    def test_givenNoInputFile_returnsNone(self):
        self.assertEqual(None, my_sort(""), "Error with input file in test:test_givenNoInputFile_returnsNone")


if __name__ == "__main__":
    unittest.main()
