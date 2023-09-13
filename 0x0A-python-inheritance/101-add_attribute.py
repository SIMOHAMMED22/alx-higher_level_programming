#!/usr/bin/python3
"""define add attribute"""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible. Raise a TypeError if not.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
                                    and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
