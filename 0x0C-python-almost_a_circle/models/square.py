#!/usr/bin/python3
"""inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Contructor for new square

        Args:
            size (int): size of the new square
            x (int): x coordinate of new square
            y (): y coordinate
            id (int): id of the new square
        """

        super().__init__(self, size, x, y, id)
