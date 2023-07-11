#!/usr/bin/python3
"""4-from_json_string.py Module"""
import json


def from_json_string(my_str):
    """This function takes a JSON string as input and returns the corresponding Python data structure .
    
          Parameters:
          my_str (str): The JSON string to be converted
    
          Returns:
          object: The Python data structure represented by the JSON string
          """
          return json.loads(my_str)
