#!/usr/bin/python3
"""
Defines a class_square
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance
        Args:
            size (int): The size of the square (default 0)
            position (tuple): The position of the square (default (0, 0))
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers
            ValueError: If size is less than 0 or position contains negative integers
        """
        self.size = size
        self.position = position

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
            value (int): The size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square
        Returns:
            The position of the square as a tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square
        Args:
            value (tuple): The position of the square as a tuple of 2 positive integers
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
            ValueError: If value contains negative integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
