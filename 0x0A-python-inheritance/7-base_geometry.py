#!/usr/bin/python3
"""
Module: base_geometry
Contains the class BaseGeometry.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an Exception with the message area() is not implemented.
        """
        def __init__(self, width, height):
            """Validate the value"""
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = heigh
