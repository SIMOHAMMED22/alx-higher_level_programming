#!/usr/bin/python3
"""Defines a function for text file-reading."""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json

    return json.loads(my_str)
