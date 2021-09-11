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
        input_file = "input.txt"
        test_list = my_sort(input_file)
        for index, val in enumerate(test_list):
            if index < len(test_list) - 1:
                self.assertLessEqual(test_list[index], test_list[index + 1], "List is not in ascending, sorted order")


if __name__ == "__main__":
    unittest.main()
