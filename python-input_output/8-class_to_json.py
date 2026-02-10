#!/usr/bin/python3
"""
Module used to convert a class instance to a dictionary representation
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a class for JSON serialization

    Args:
        obj: Instance of a class to be converted to a dictionary

    Returns:
        dict: Dictionary representation of the object's attributes
    """
    return vars(obj)
