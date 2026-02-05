#!/usr/bin/python3


class VerboseList(list):
    """A list subclass that prints notification messages.

    This class extends the built-in list class to provide
    verbose output when items are added, extended, removed, or popped.
    """

    def append(self, item):
        """Append an item to the list and print a notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extend the list with items and print a notification.

        Args:
            item: An iterable of items to extend the list with.
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification.

        Args:
            item: The item to remove from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at the given index.

        Args:
            index: The index of the item to pop (default: -1, last item).
        """
        print(f"Popped [{index}] from the list.")
        super().pop(index)
