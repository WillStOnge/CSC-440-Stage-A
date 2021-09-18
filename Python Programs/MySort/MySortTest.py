"""
MySortTest.py

Programmer: Justin Gallagher
Course: CSC440

MySortTest.py contains two unit tests for the method my_sort() in MySort.py
"""

import unittest
from MySort import my_sort


class MySortTest(unittest.TestCase):
    """
        Defines test cases for my_sort()
    """
    def test_givenInputFile_returnsSortedList(self):
        """
            Given an input file containing integer values, test that the my_sort method
            correctly returns an ascending, sorted list.
        """
        test_list = my_sort("input.txt")
        for index in range(len(test_list) - 1):
            self.assertLessEqual(test_list[index], test_list[index + 1],
                                 "List is not in ascending, sorted order in test:test_givenInputFile_returnsSortedList")

    def test_givenNoInputFile_returnsFileNotFoundError(self):
        """
            Given no input file, test that the my_sort method correctly raises a FileNotFoundError.
        """
        with self.assertRaises(FileNotFoundError):
            test_list = my_sort("")


if __name__ == "__main__":
    unittest.main()
