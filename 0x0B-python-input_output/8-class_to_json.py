#!/usr/bin/python3
""" function that returns the dictionary. """


def class_to_json(obj):
    """ Function retuns dictionary """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
def class_to_json(obj):
    """
    Returns a dictionary representation of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing serializable attributes of the object.

    """
    json_dict = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
