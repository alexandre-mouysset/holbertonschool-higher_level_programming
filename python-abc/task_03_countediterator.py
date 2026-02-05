#!/usr/bin/python3


class CountedIterator:
    """An iterator wrapper that keeps track of the number of items iterated.

    This class takes an iterable object and provides an iterator interface
    while counting how many items have been iterated through.
    """

    def __init__(self, iterator):
        """Initialize the CountedIterator.

        Args:
            iterator: An iterable object to wrap.
        """
        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        """Get the current count of iterated items.

        Returns:
            int: The number of items that have been iterated through.
        """
        return self.counter

    def __next__(self):
        """Get the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator.
=
        Raises:
            StopIteration: When there are no more items to iterate.
        """
        self.counter += 1
        return next(self.iterator)
