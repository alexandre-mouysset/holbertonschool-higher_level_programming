#!/usr/bin/python3
"""
Module used to read and print the contents of a text file
"""


def read_file(filename=""):
    """
    Reads a file and prints its contents to stdout

    Args:
        filename (str): Path to the file to read

    Returns:
        None
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
