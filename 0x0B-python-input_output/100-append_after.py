#!/usr/bin/python3

import os

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert.

    """
    temp_filename = filename + ".tmp"  # Temporary file to write the modified content

    with open(filename, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            temp_file.write(line)  # Write the original line

            if search_string in line:
                temp_file.write(new_string + "\n")  # Write the new line after matching line

    # Replace the original file with the modified content
    os.replace(temp_filename, filename)
