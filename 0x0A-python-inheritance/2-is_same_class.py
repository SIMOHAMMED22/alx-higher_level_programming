#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)


a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
