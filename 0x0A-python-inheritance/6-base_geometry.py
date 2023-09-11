#!/usr/bin/python3
"""Defining an object attribute lookup function."""


class BaseGeometry:
    """
    A class representing base geometry.

    Methods:
        area(self): Raises an Exception with
        the message 'area() is not implemented'.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always raises an Exception with the specified message.
        """
        raise Exception('area() is not implemented')
