#!/usr/bin/python3

"""square class"""


class Square:
    """defines a square
    Private attributes size and position with getters and setters,
    and public methods area and my_print
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
            size (int): size of the square. Defaults to 0
            position (tuple): The position  of the square.
                Defaults to (0, 0)
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size

        Returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size of square
        Args:
            value (int): size of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter for position
        Returns position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position of square
        Args:
            value (tuple): position of square
        """
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.position = value

    def area(self):
        """Area method
        Returns the area of the current square
        """
        return self.__size * self.__size

    def my_print(self):
        """Print method
        Prints to stdout the current square with the character #
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")

            print()
