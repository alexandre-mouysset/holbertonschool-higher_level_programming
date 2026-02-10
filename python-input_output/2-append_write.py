#!/usr/bin/python3
"""
Module used to append text to a file
"""


def append_write(filename="", text=""):
    """
    Appends text to the end of a file

    Args:
        filename (str): Path to the file to append to
        text (str): Content to append to the file

    Returns:
        int: Number of characters appended to the file
    """
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(text)
        return (len(text))
