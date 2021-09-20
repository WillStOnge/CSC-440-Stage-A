"""
ArithTest.py
Author Cory Knoll
CSC 440
"""

import unittest
from Arith import Arith

class ArithTest(unittest.TestCase):
    """
    Defines test cases for add() and sub().
    """
    def test_getSum_twoNumbers(self):
        """
        Given 2 integers, the add method should return the correct result.
        """
        self.assertEqual(17, Arith().add(8, 9))

    def test_getDiff_twoNumbers(self):
        """
        Given 2 integers, the sub method should return the correct result.
        """
        self.assertEqual(4, Arith().sub(11, 7))
