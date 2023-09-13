#!/usr/bin/python3
"""
Define a class of Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute
            names to include in the dictionary. Default is None.

        Returns:
            dict: A dictionary containing the
            specified attributes of the Student.

        """
        student_dict = {}
        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)
        return student_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys
            are attribute names and values are the new values.

        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
