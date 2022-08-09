"""Queue data type using an array."""

from Array import Array

class Queue(Array):
    """Upon initialising the Queue, an integer value must be provided to assign the size of the array."""
    def __init__(self, size: int):
        Array.__init__(self, size)
        self.count = 0

    def __len__(self):
        """Returns the length of the Queue."""
        return self.count

    def is_empty(self):
        """Returns True if the Queue is empty and False if it has contents."""
        return self.count == 0

    def is_full(self):
        """Returns True if the Queue Array is full and False if it has space."""
        return self.count == self.size

    def enqueue(self, x):
        """Adds x to the end of the Queue. Raises an exception if the Queue is full."""
        if self.count == self.size:
            raise IndexError("Queue is full.")
        self._data[self.count] = x
        self.count += 1
        
    def dequeue(self):
        """Removes and returns the element at the start of the Queue. Raises an exception if the Queue is empty."""
        if self.count == 0:
            raise IndexError("Queue is empty.")
        result = self._data[0]
        self._data[0:self.count-1] = self._data[1:self.count]
        self._data[self.count-1] = None
        self.count -= 1
        return result

    def first(self):
        """Returns the first element from the Queue but does not remove it. Raises and exception if the Queue is empty."""
        if self.count == 0:
            raise AttributeError("Queue is empty")
        return self._data[0]
