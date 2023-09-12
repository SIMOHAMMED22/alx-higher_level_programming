#!/usr/bin/python3
"""Defines a function for text file-reading."""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized to JSON and saved.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    import json

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
