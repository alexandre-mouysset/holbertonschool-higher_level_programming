#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses.

This module provides an abstract Animal class using ABC
with concrete implementations for Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract animal class.

    This class represents a generic animal with an abstract method
    that must be implemented by all subclasses.
    """
    @abstractmethod
    def sound(self) -> str:
        """Abstract method returning the animal's sound.

        Returns:
            str: The sound produced by the animal.
        """
        ...


class Dog(Animal):
    """A dog class that inherits Animal.

    This class represents a dog with its specific sound.
    """
    def sound(self) -> str:
        """Returns the dog's sound.

        Returns:
            str: The sound 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """A cat class that inherits Animal.

    This class represents a cat with its specific sound.
    """
    def sound(self) -> str:
        """Returns the cat's sound.

        Returns:
            str: The sound 'Meow'.
        """
        return "Meow"
