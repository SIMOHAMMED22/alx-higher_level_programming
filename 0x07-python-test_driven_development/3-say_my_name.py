#!/usr/bin/python3
"""
matrix division module
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first_name> <last_name>"

    :param first_name: The first name (string)
    :param last_name: The last name (string, optional, default is "")
    :raises TypeError: If either first_name or last_name is not a string
    """
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string")

    if last_name:
        full_name = f"My name is {first_name} {last_name}"
    else:
        full_name = f"My name is {first_name}"

    print(full_name)
