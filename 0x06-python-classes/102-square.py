#!/usr/bin/python3
"""
Defines a class Square that represents a square
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
            size (float or int): The size of the square
        Raises:
            TypeError: If size is not a number
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (float or int): The size to be set
        Raises:
            TypeError: If value is not a number
            ValueError: If value is less than 0
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison operator ==
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Inequality comparison operator !=
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Greater than comparison operator >
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal to comparison operator >=
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Less than comparison operator <
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal to comparison operator <=
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
