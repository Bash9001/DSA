from queue import Empty
import PriorityQueueBase
from LinkedLists import PositionalLinkedList

class SortedPriorityQueue(PriorityQueueBase):
    """A minimum oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalLinkedList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        new = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_after(walk, new)

    def min(self):
        """Returns the (key, value) tuple with the minimum key, without removing it."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return the (key, value) tuple with the minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        p = self._data.first()
        item = p._data.delete(p)
        return (item._key, item._value)
