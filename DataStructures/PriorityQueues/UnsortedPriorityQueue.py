from queue import Empty
import PriorityQueueBase
from LinkedLists import PositionalLinkedList

class UnsortedPriorityQueue(PriorityQueueBase):
    """A minimum oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalLinkedList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        """A non-public class to return the position of the item with the minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        smallest = self._data.first()
        walk = self._data.after(smallest)
        while walk is not None:
            if walk.element() < smallest.element():
                smallest = walk
            walk = self._data.after(walk)
        return smallest

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Returns the (key, value) tuple with the minimum key, without removing it."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return the (key, value) tuple with the minimum key."""
        p = self._find_min()
        item = p._data.delete(p)
        return (item._key, item._value)
