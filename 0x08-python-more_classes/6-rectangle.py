#!/usr/bin/python3

"""Rectangle module."""


class Rectangle:
    """Rectangle Class."""
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with optional width and height attributes."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Generate a string representation of the rectangle using '#' symbols."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Generate a string representation that can recreate an instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted and decrement the number_of_instances attribute."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
