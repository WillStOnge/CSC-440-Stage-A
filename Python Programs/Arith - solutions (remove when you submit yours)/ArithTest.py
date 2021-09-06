"""
ArithTest.py

CSC440
"""

import unittest
from Arith import Arith

class MyArithTest(unittest.TestCase):
    """
        Test cases for mysort()
    """

    def test_givenTwoNumbers_whenAddCalled_returnsTheirSum(self):
        self.assertEqual(10, Arith().add(7, 3))

    def test_givenTwoNumbers_whenSubCalled_returnsTheirDifference(self):
        self.assertEqual(5, Arith().sub(10, 5))
