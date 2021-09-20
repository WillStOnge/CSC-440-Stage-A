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
        """
            Given an input file containing integer values, and the integer value 8,
            test that the my_search method correctly returns the index 6 verifying
            that 8 is in the list.
        """
        index = my_search("input.txt", 8)
        self.assertEqual(index, 6)

    def test_search_fail(self):
        """
            Given an input file containing integer values, and the integer value 0,
            test that the my_search method correctly returns -1 verifying that
            0 is not in the list.
        """
        index = my_search("input.txt", 0)
        self.assertEqual(index, -1)

    def test_open_file(self):
        """
            Given an input file that does not exist, test that the my_search method
            correctly raises a FileNotFoundError.
        """
        with self.assertRaises(FileNotFoundError):
            index = my_search("my_file.txt", 8)


if __name__ == "__main__":
    unittest.main()

