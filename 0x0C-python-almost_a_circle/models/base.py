#!/usr/bin/python3

"""
This module defines the Base class.
"""

import json
import turtle


class Base:
    """
    The Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): The id value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: A double pointer to a dictionary.

        Returns:
            Base: An instance with attributes set according to the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            dummy = None

        dummy.update(**dictionary)  # Update the dummy instance with the dictionary
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [
                    cls.create(**dictionary) for dictionary in dictionaries
                ]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.setup(800, 600)  # Set the screen dimensions

        # Create a turtle for drawing rectangles
        rectangle_turtle = turtle.Turtle()
        rectangle_turtle.color("red")
        rectangle_turtle.pensize(2)

        # Draw rectangles
        for rectangle in list_rectangles:
            rectangle_turtle.penup()
            rectangle_turtle.goto(rectangle.x, rectangle.y)
            rectangle_turtle.pendown()
            rectangle_turtle.forward(rectangle.width)
            rectangle_turtle.right(90)
            rectangle_turtle.forward(rectangle.height)
            rectangle_turtle.right(90)
            rectangle_turtle.forward(rectangle.width)
            rectangle_turtle.right(90)
            rectangle_turtle.forward(rectangle.height)
            rectangle_turtle.right(90)

        # Create a turtle for drawing squares
        square_turtle = turtle.Turtle()
        square_turtle.color("blue")
        square_turtle.pensize(2)

        # Draw squares
        for square in list_squares:
            square_turtle.penup()
            square_turtle.goto(square.x, square.y)
            square_turtle.pendown()
            for _ in range(4):
                square_turtle.forward(square.size)
                square_turtle.right(90)

        turtle.done()
