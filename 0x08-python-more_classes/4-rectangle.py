#!/usr/bin/python3

"""Rectangle module."""


class Rectangle:
    """Rectangle Class."""

    def __init__(self, width=0, height=0):
        """__init__ rectangle constructor."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """__str__ repersentation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        _str = ""
        for _ in range(self.height):
            _str += "#" * self.width
            _str += "\n" if _ + 1 < self.height else ""
        return _str

    def __repr__(self):
        """Representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
