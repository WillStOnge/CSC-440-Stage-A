"""
Arith.py
Author: Cory Knoll
CSC 440
"""

class Arith(object):
    def __init__(self):
        """
        Default no-arg constructor for the Arith class.

        >>> Arith().add(1, 2)
        3

        >>> Arith().sub(1, 2)
        -1
        """
        pass

    def add(self, x, y):
        """
        Adds 2 numbers together and returns the result.

        :param x: First operand in the addition operation.
        :param y: Second operand in the addition operation.
        :returns: The sum of x and y.

        >>> Arith().add(1, 2)
        3

        >>> Arith().add(9, 6)
        15
        """
        return (x + y)
        
    def sub(self, x, y):
        """
        Subtracts 2 numbers together and returns the result.

        :param x: First operand in the subtraction operation.
        :param y: Second operand in the subtraction operation.
        :returns: The sum of x and -y.

        >>> Arith().sub(1, 2)
        -1

        >>> Arith().sub(9, 6)
        3
        """
        return (x - y)
