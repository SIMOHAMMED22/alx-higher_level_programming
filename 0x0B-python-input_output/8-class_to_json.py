#!/usr/bin/python3

"""
Converts an object to a JSON-serializable data structure.

:param obj: The object to be converted.
:return: The JSON-serializable representation of the object.
"""


def class_to_json(obj):
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    else:
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))
