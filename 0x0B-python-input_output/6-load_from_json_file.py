#!/usr/bin/python3
"""Defines a function for text file-reading."""


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    import json

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
