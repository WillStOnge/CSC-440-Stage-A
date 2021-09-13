"""
MySearch.py
Programmer: Anthony Bosch
Course: CSC440
"""

import os.path


def my_search(input_file, value):
    if not os.path.isfile(input_file):
        raise FileNotFoundError
    try:
        with open(input_file, "r") as in_file:
            return [int(i) for i in in_file.read().splitlines()].index(value)
    except ValueError:
        return -1
