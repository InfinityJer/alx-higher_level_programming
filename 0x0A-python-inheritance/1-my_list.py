#!/usr/bin/python3

class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print the list, but sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
