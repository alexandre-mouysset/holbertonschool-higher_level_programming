#!/usr/bin/python3
"""
Module used to read a JSON file and return its deserialized object
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): Path to the JSON file to load from

    Returns:
        object: Python object deserialized from the JSON file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        json_str = f.read()
        return json.loads(json_str)
