#!/usr/bin/python3
"""Defining an object attribute lookup function."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
