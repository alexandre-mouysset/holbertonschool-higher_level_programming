#!/usr/bin/python3
"""Module demonstrating multiple inheritance with Fish, Bird and
FlyingFish classes"""


class Fish:
    """Represents a fish with swimming and habitat behaviors.

    This class provides basic behaviors for a fish that can swim
    and has a defined habitat.
    """

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat information."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying and habitat behaviors.

    This class provides basic behaviors for a bird that can fly
    and has a defined habitat.
    """

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat information."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that inherits from both Fish and Bird.

    This class demonstrates multiple inheritance, combining the abilities
    and behaviors of both Fish and Bird classes. A flying fish can both
    swim in water and fly in the air, and exists in both environments.
    """

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish's habitat information."""
        print("The flying fish lives both in water and the sky!")
