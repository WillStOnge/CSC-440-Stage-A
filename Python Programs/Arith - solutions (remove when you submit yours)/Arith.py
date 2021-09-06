"""
Arith.py

Programmer: Samuel Cho
Course: CSC440
"""


class Arith(object):
    """
        Simply object for adding and subtracting
    """

    def __init__(self): pass

    def add(self, x, y):
        """
        :param x:
            A numeric
        :param y:
            A numeric
        :return:
            X + Y

        Examples:

        >>> Arith().add(-4, 4)
        0
        >>> Arith().add(92, 8)
        100
        >>> Arith().add(25, 25)
        50
        """
        return x + y

    def sub(self, x, y):
        """
        :param x:
            A numeric
        :param y:
            A numeric
        :return:
            X - Y

        Examples:

        >>> Arith().sub(10 , 1)
        9
        >>> Arith().sub(4, 10)
        -6
        >>> Arith().sub (100,100)
        0
        """
        return x - y
