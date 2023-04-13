#!/usr/bin/python3
"""
A module that has a class Mylist then has a function that inherits the list
in a sorted format.
"""
class MyList(list):
    """
    A list that provides a print_sorted() method to print the list
    in sorted order
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
