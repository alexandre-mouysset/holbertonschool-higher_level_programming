#!/usr/bin/python3
"""
Module for pickling and unpickling custom objects
"""
import pickle


class CustomObjet:
    """
    A custom class for demonstrating pickle serialization

    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObjet instance

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes to stdout

        Returns:
            None
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file using pickle

        Args:
            filename (str): Path to the file to save

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a pickle file

        Args:
            filename (str): Path to the pickle file to load

        Returns:
            CustomObjet: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
