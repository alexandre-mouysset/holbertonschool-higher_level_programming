#!/usr/bin/python3
"""
Module for basic serialization and deserialization of data to/from JSON files
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to JSON and saves it to a file

    Args:
        data (dict): The data to serialize
        filename (str): Path to the file to save

    Returns:
        None
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file

    Args:
        filename (str): Path to the file to load

    Returns:
        dict: The deserialized data
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
