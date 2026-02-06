#!/usr/bin/python3
"""Module demonstrating mixins with SwimMixin, FlyMixin and Dragon classes."""


class SwimMixin:
    """Mixin class that provides swimming behavior.

    This mixin can be combined with other classes to add
    the ability to swim to any creature.
    """

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying behavior.

    This mixin can be combined with other classes to add
    the ability to fly to any creature.
    """

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim and fly.

    This class combines SwimMixin and FlyMixin to create a dragon creature
    that has the abilities of both swimming and flying, plus its own
    unique roaring behavior.
    """

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
