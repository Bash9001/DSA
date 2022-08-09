"""Dequeue data type using an array."""

from Array import Array

class Dequeue(Array):
    """Upon initialising the Dequeue, an integer value must be provided to assign the size of the array."""
    def __init__(self, size: int):
        Array.__init__(self, size)
        self.count = 0

    def __len__(self):
        """Returns the length of the Dequeue."""
        return self.count

    def is_empty(self):
        """Returns True if the Dequeue is empty and False if it has contents."""
        return self.count == 0

    def is_full(self):
        """Returns True if the Dequeue Array is full and False if it has space."""
        return self.count == self.size

    def add_first(self, x):
        """Adds x to the front of the Dequeue. Raises an exception if the Dequeue is full."""
        if self.count == self.size:
            raise IndexError("Dequeue is full.")
        self._data[1:self.count+1] = self._data[0:self.count]
        self._data[0] = x
        self.count += 1

    def add_last(self, x):
        """Adds x to the end of the Dequeue. Raises an exception if the Dequeue is full."""
        if self.count == self.size:
            raise IndexError("Dequeue is full.")
        self._data[self.count] = x
        self.count += 1
        
    def remove_first(self):
        """Removes and returns the first element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if self.count == 0:
            raise IndexError("Dequeue is empty.")
        result = self._data[0]
        self._data[0:self.count-1] = self._data[1:self.count]
        self._data[self.count-1] = None
        self.count -= 1
        return result

    def remove_last(self):
        """Removes and returns the last element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if self.count == 0:
            raise IndexError("Dequeue is empty.")
        result = self._data[self.count-1]
        self._data[self.count-1] = None
        self.count -= 1
        return result

    def first(self):
        """Returns the first element from the Dequeue but does not remove it. Raises and exception if the Dequeue is empty."""
        if self.count == 0:
            raise AttributeError("Dequeue is empty")
        return self._data[0]

    def last(self):
        """Returns the last element from the Dequeue but does not remove it. Raises and exception if the Dequeue is empty."""
        if self.count == 0:
            raise AttributeError("Dequeue is empty")
        return self._data[self.count-1]
