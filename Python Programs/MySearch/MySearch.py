"""
MySearch.py
Programmer: Anthony Bosch
Course: CSC440
"""

import os.path


def my_search(input_file, value):
    """
    Search a list of integers for a specific value.

    :param input_file: The file with list of integers
    :param value:  The value being searched in the list
    :return: returns the value if found, -1 if not found
    :raises: FileNotFoundError: Raised if the file cannot be found

    ===========================

    Using ``MySearch``
    ------------------

    This is an example text file in reStructuredText format.  First import
    ``my_search`` from the ``MySearch`` module.

    Now use it:

    Given an input file containing integer values and an integer value of 8,
    the function will return 6, as the value 8 is in the 6th index of the list of values.
    >>> my_search("input.txt", 8)
    6

    Given an input file containing integer values and an integer value of 1,
    the function will return -1, as the value 1 is not in the list of values.
    >>> my_search("input.txt", 1)
    -1

    Given an input file that does not exist, a FileNotFoundError will be raised.
    >>> my_search("", 8)
    Traceback (most recent call last):
     ...
    FileNotFoundError
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError
    try:
        with open(input_file, "r") as in_file:
            return [int(i) for i in in_file.read().splitlines()].index(value)
    except ValueError:
        return -1
