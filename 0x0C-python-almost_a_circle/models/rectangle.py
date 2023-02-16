#!/usr/bin/python3

"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for new rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the new rectangle
            y (int): y coordinate of new rectangle
            id (int): Id of the new rectangle

        Raises:
            TypeError: if either width or height is not an integer
            ValueError: if either width or height <= 0
            TypeError: if either x or y is not an int
            ValueError: if either x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter for y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Public method
        Returns the area value of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Public method
        Prints in stdout the rectangle instance with the character `#`
        """

        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        string = (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

        return string
