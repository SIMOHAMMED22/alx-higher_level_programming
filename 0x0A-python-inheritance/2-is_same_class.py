#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
