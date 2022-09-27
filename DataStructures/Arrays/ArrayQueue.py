from queue import Empty, Full
from _Array import _Array

class Queue(_Array):
    """Queue data type using an array. An integer value must be provided to assign the size of the array."""

    def enqueue(self, x):
        """Adds x to the end of the Queue. Raises an exception if the Queue is full."""
        if self._count == self._size:
            raise Full("Queue is full.")
        self._data[self._count] = x
        self._count += 1
        
    def dequeue(self):
        """Removes and returns the element at the start of the Queue. Raises an exception if the Queue is empty."""
        if self._count == 0:
            raise Empty("Queue is empty.")
        result = self._data[0]
        self._data[0:self._count-1] = self._data[1:self._count]
        self._data[self._count-1] = None
        self._count -= 1
        return result

    def first(self):
        """Returns the first element from the Queue but does not remove it. Raises and exception if the Queue is empty."""
        if self._count == 0:
            raise Empty("Queue is empty")
        return self._data[0]
