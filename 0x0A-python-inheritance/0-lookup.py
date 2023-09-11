#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (object): The object to look up.

    Returns:
    list: A list of attribute and method names.
    """
    return dir(obj)
