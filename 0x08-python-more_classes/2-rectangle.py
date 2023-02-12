#!/usr/bin/python3
"""Area and perimeter of a rectangle"""


class Rectangle:
    """Defines a rectangle based on 1-rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor for new rectangle

        Args:
            width (int, optional): width of new rectangle. Default is 0
            height (int, optional): height of new rectangle. Default value is 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method for getting area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method for getting rectangle perimeter"""
        return (self.__width + self.__height) * 2
