#!/usr/bin/python3
"""Create a class that inherit from int """


class MyInt(int):

    def __eq__(self, other):
        """
        Override the equality (==) operator to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality (!=) operator to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
