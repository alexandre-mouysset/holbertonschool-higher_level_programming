#!/usr/bin/python3
"""
Module used to define a Student class and serialize it to JSON
"""


class Student:
    """
    Represents a student with basic information
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of student with selective attribut

        Args:
            attrs: Optional list of attribute names to include in the output
                          If valid, only these attributes are returned.

        Returns:
            dict: Dictionary containing the specified student attributes,
                  or all attributes if attrs is not a valid list of strings
        """
        if isinstance(attrs, list) and all(
           isinstance(item, str) for item in attrs):
            obj_dict = vars(self)
            filtered_dict = {}
            for key in attrs:
                if key in obj_dict:
                    filtered_dict[key] = obj_dict[key]
            return filtered_dict
        else:
            return vars(self)
