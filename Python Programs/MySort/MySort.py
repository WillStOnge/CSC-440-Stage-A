"""
MySort.py

Programmer: Justin Gallagher
Course: CSC440
"""


def my_sort(input_file):
    input_list = []
    in_file = open(input_file, "r")
    for line in in_file:
        input_list.append(int(line))
    in_file.close()
    input_list.sort()
    return input_list
