"""
MySort.py

Programmer: Justin Gallagher
Course: CSC440
"""


def my_sort(input_file):
    try:
        with open(input_file, "r") as in_file:
            return sorted(int(x) for x in in_file.read().splitlines())
    except FileNotFoundError:
        print("File does not exist")
