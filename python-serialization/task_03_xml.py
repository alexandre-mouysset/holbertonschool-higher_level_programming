#!/usr/bin/python3
"""
Module for serializing and deserializing data to/from XML files
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): Path to the XML file to write

    Returns:
        bool: True if serialization was successful
    """
    root = ET.Element("data")
    for k, v in dictionary.items():
        ET.SubElement(root, k).text = str(v)
    ET.ElementTree(root).write(filename)
    return True


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary

    Args:
        filename (str): Path to the XML file to read

    Returns:
        dict: The deserialized dictionary
    """
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
