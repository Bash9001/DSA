from queue import Empty, Full
from _Array import _Array

class Dequeue(_Array):
    """Dequeue data type using an array. An integer value must be provided to assign the size of the array."""

    def add_first(self, x):
        """Adds x to the front of the Dequeue. Raises an exception if the Dequeue is full."""
        if self._count == self._size:
            raise Full("Dequeue is full.")
        self._data[1:self._count+1] = self._data[0:self._count]
        self._data[0] = x
        self._count += 1

    def add_last(self, x):
        """Adds x to the end of the Dequeue. Raises an exception if the Dequeue is full."""
        if self._count == self._size:
            raise Full("Dequeue is full.")
        self._data[self._count] = x
        self._count += 1
        
    def remove_first(self):
        """Removes and returns the first element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if self._count == 0:
            raise Empty("Dequeue is empty.")
        result = self._data[0]
        self._data[0:self._count-1] = self._data[1:self._count]
        self._data[self._count-1] = None
        self._count -= 1
        return result

    def remove_last(self):
        """Removes and returns the last element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if self._count == 0:
            raise Empty("Dequeue is empty.")
        result = self._data[self._count-1]
        self._data[self._count-1] = None
        self._count -= 1
        return result

    def first(self):
        """Returns the first element from the Dequeue but does not remove it. Raises and exception if the Dequeue is empty."""
        if self._count == 0:
            raise Empty("Dequeue is empty")
        return self._data[0]

    def last(self):
        """Returns the last element from the Dequeue but does not remove it. Raises and exception if the Dequeue is empty."""
        if self._count == 0:
            raise Empty("Dequeue is empty")
        return self._data[self._count-1]
