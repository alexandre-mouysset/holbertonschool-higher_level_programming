#!/usr/bin/python3
"""
Module used to define a Student class with selective JSON
serialization and deserialization
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
        Returns the dictionary representation of a student
        with selective attributes

        Args:
            attrs (list): Optional list of attribute names to
                         include in the output. If valid, only
                         these attributes are returned.

        Returns:
            dict: Dictionary containing the specified student
                  attributes, or all attributes if attrs is
                  not a valid list of strings
        """
        if isinstance(attrs, list) and all(
                isinstance(item, str) for item in attrs):

            obj_dict = vars(self)
            sorted_dict = {}
            for key in attrs:
                if key in obj_dict:
                    sorted_dict[key] = obj_dict[key]
            return sorted_dict

        else:
            return vars(self)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from a dictionary

        Args:
            json (dict): Dictionary containing attribute names
                        and values to update

        Returns:
            None
        """

        if "first_name" in json:
            self.first_name = json["first_name"]

        if "last_name" in json:
            self.last_name = json["last_name"]

        if "age" in json:
            self.age = json["age"]
