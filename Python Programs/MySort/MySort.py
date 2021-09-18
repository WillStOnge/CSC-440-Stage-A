"""
MySort.py

Programmer: Justin Gallagher
Course: CSC440

MySort.py contains the a sorting method called my_sort()
"""


def my_sort(input_file):
    """
    Reads a given input file for integer values, sorts them in
    ascending order, and returns a list of the sorted values.

    :param input_file: The file containing the values to be sorted
    :return: Sorted list of integer values
    :raises: FileNotFoundError: Raised if the file cannot be found

    ----------------
    Using ``MySort``
    ----------------

    First import ``my_sort`` from the ``MySort`` module to use it.

    For example, given an input file containing integer values,
    the function returns the sorted list.
    >>> my_sort("input.txt")
    [2, 8, 17, 19, 22, 27, 29, 31, 36, 37, 38, 46, 47, 56, 64, 65, 66, 79, 84, 85, 86, 90, 93, 98, 99]

    Given a file that does not exist, a FileNotFoundError will be raised.
    >>> my_sort("")
    Traceback (most recent call last):
     ...
    FileNotFoundError
    """
    try:
        with open(input_file, "r") as in_file:
            return sorted(int(x) for x in in_file.read().splitlines())
    except FileNotFoundError:
        raise FileNotFoundError
