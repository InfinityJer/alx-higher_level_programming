#!/usr/bin/python3
"""
Module: inherits_from
Contains a function that checks if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
