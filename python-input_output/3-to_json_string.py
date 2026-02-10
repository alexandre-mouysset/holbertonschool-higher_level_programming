#!/usr/bin/python3
"""
Module used to serialize an object to a JSON string
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        my_obj: Object to be serialized to JSON

    Returns:
        str: JSON string representation of the object
    """
    return json.dumps(my_obj)
