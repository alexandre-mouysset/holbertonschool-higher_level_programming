#!/usr/bin/env python3
"""Module defining an animal class hierarchy using ABC."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing a generic animal."""
    @abstractmethod
    def sound(self) -> str:
        """Abstract method returning the animal's sound.

        Returns:
            str: The sound produced by the animal.
        """
        ...


class Dog(Animal):
    """Class representing a dog."""
    def sound(self) -> str:
        """Returns the dog's sound.

        Returns:
            str: The sound 'bark'.
        """
        return "bark"


class Cat(Animal):
    """Class representing a cat."""
    def sound(self) -> str:
        """Returns the cat's sound.

        Returns:
            str: The sound 'Meow'.
        """
        return "Meow"
