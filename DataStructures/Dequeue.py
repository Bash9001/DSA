"""Dequeue data type using a list."""

class Dequeue:
    def __init__(self):
        self._data = []

    def __len__(self):
        """Returns the length of the Dequeue."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the Dequeue is empty and False if it has contents."""
        return len(self._data) == 0

    def add_first(self, x):
        """Adds x to the front of the Dequeue"""
        self._data[1:] = self._data[0:]
        self._data[0] = x

    def add_last(self, x):
        """Adds x to the end of the Dequeue."""
        self._data.append(x)
        
    def remove_first(self):
        """Removes and returns the first element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if len(self._data) == 0:
            raise IndexError("Queue is empty.")
        result = self._data[0]
        self._data[0:] = self._data[1:]
        self._data[:-1]
        return result

    def remove_last(self):
        """Removes and returns the last element of the Dequeue. Raises an exception if the Dequeue is empty."""
        if self.count == 0:
            raise IndexError("Dequeue is empty.")
        result = self._data[-1]
        self._data[:-1]
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
        return self._data[-1]
