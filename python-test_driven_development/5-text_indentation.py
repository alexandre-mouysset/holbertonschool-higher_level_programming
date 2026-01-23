#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', ':'.

    Args:
        text: String to format

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for i in text:
        line = line + i
        if i == "." or i == "?" or i == ":":
            print(line, end="")
            print()
            line = ""
    if line:
        print(line)
