#!/usr/bin/python3
"""
Module used to write text to a file
"""


def write_file(filename="", text=""):
    """
    Writes text to a file, creating it if it doesn't exist

    Args:
        filename (str): Path to the file to write to
        text (str): Content to write to the file

    Returns:
        int: Number of characters written to the file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(text)
        return len(text)
