#!/usr/bin/python3

"""
Module: lookup
Contains a function that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
