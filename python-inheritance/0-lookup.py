#!/usr/bin/python3
"""lookup function module."""


def lookup(obj):
    """Return list of available attributes and methods for an object."""
    return dir(obj)
