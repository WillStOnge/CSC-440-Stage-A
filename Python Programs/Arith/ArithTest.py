"""
ArithTest.py
Author Cory Knoll
CSC 440
"""

import unittest
from Arith import Arith

class ArithTest(unittest.TestCase):
    def test_getSum_twoNumbers(self):
        self.assertEqual(17, Arith().add(8, 9))

    def test_getDiff_twoNumbers(self):
        self.assertEqual(4, Arith().sub(11, 7))