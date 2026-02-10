#!/usr/bin/python3
"""
Module used to write a JSON representation of an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of an object to a file

    Args:
        my_obj: Object to be serialized to JSON
        filename (str): Path to the file to write to

    Returns:
        None
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
