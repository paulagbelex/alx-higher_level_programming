#!/usr/bin/python3
"""
Square module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): size of the square.
            x (int): horizontal offset.
            y (int): vertical offset.
            id (int): unique identifier.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square instance.

        Returns:
            str: string representation of the square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, attr in enumerate(args):
                setattr(self, attrs[i], attr)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square instance.

        Returns:
            dict: dictionary representation of the square instance.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
