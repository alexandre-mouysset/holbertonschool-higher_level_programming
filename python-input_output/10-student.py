#!/usr/bin/python3
"""
Module used to enhance the Student class with selective JSON serialization
"""

Student = __import__("9-student").Student


def to_json(self, attrs=None):
    """
    Returns the dictionary representation of a student with selective attribute

    Args:
        self: The student instance
        attrs (list): Optional list of attribute names to include in the output
                     If valid, only these attributes are returned.

    Returns:
        dict: Dictionary containing the specified student attributes,
              or all attributes if attrs is not a valid list of strings
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
