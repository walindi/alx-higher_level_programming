#!/usr/bin/python3
"""defines a rectangle and finds it's area and perimeter"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor for new rectangle

        Args:
            width (int, optional): width of new rectangle. Default is 0
            heright (int, optional): height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value (int): width of rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height of rectangle
        Args:
            value (int): height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to return perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns printable representation of the rectangle
        prints the rectangle using # character"""

        if self.__width == 0 or self.__height == 0:
            return ""

        characters = ""
        for h in range(self.__height):
            characters += "{}".format("#" * self.__width)
            if h < self.__height - 1:
                characters += "\n"

        return characters
