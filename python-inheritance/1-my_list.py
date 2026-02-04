#!/usr/bin/python3
"""MyList class module."""


class Mylist(list):
    """A list subclass with printing utilities."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
