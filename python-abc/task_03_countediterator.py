#!/usr/bin/python3

class CountedIterator:
    """Iterator wrapper that counts the number of items returned.

    This class wraps any iterable object and provides an iterator interface,
    keeping track of how many items have been iterated so far.
    """

    def __init__(self, iterator):
        """Initialize the CountedIterator with an iterable and a counter.

        Args:
            iterator: Any iterable object (like a list, tuple) to wrap.
        """
        self._iterator = iter(iterator)
        self._counter = 0

    def get_count(self):
        """Return the number of items that have been iterated so far.

        Returns:
            int: Total number of elements returned by the iterator.
        """
        return self._counter

    def __next__(self):
        """Return the next item from the iterator and increment the counter.

        Each call to this method increases the internal counter by 1.
        If the iterator is exhausted, StopIteration is raised.

        Returns:
            The next element from the wrapped iterator.

        Raises:
            StopIteration: If there are no more elements to return.
        """
        self._counter += 1
        return next(self._iterator)
