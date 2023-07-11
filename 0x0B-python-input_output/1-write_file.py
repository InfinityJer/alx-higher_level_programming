#!/usr/bin/python3
"""1-write_file.py Module"""

def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and returns the number of characters written.
    
    Parameters:
    filename (str): The name of the file to write to
    text (str): The string to write to the file
    
    Returns:
    int: The number of characters written to the file
    """
    with open(filename, mode='w', encoding='utf8') as f:
        return f.write(text)
