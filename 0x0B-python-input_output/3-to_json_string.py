#!/usr/bin/python3
"""3-to_json_string.py Module"""
import json


def to_json_string(my_obj):
    """
    This function takes an object as input and returns its JSON representation as a string.

    Parameters:
    my_obj: The object to be serialized into JSON

    Returns:
    str: The JSON representation of the object
    """
    return json.dumps(my_obj)
