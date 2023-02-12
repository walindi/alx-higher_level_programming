#!/usr/bin/python3
"""1-rectangle"""


class Rectangle:
    """Defines a rectangle based on 0-rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor for new rectangle
        Args:
            width (int, optional): width of new rectangle. Default is 0
            height (int, optional): height of new reactangle. Defaults to 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width of rectangle
        Args:
            value (int): value of width to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height of rectangle
        Args:
            value (int): height to set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
