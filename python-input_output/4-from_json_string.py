#!/usr/bin/python3
"""
Module used to deserialize a JSON string to an object
"""
import json


def from_json_string(my_str):
    """
    Returns an object deserialized from a JSON string

    Args:
        my_str (str): JSON string to be deserialized

    Returns:
        object: Python object representation of the JSON string
    """
    return json.loads(my_str)
