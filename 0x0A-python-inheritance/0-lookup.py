#!/usr/bin/python3
"""Defines objrct attribute lookup function"""
def lookup(obj):
        """Returns a list of attributes and methods of the given object"""
        return (dir(obj))
