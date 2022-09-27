from queue import Empty

class Dequeue:
    """Dequeue data type using a list."""
    def __init__(self):
        self._data = []

    def __len__(self):
        """Returns the length of the dequeue."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the dequeue is empty."""
        return len(self._data) == 0

    def add_first(self, x):
        """Adds x to the front of the dequeue"""
        self._data[1:] = self._data[0:]
        self._data[0] = x

    def add_last(self, x):
        """Adds x to the end of the dequeue."""
        self._data.append(x)
        
    def remove_first(self):
        """Removes and returns the first element of the dequeue."""
        if len(self._data) == 0:
            raise Empty("Queue is empty.")
        result = self._data[0]
        self._data[0:] = self._data[1:]
        self._data[:-1]
        return result

    def remove_last(self):
        """Removes and returns the last element of the dequeue."""
        if self.count == 0:
            raise Empty("Dequeue is empty.")
        result = self._data[-1]
        self._data[:-1]
        return result

    def first(self):
        """Returns the first element from the dequeue but does not remove it."""
        if self.count == 0:
            raise Empty("Dequeue is empty")
        return self._data[0]

    def last(self):
        """Returns the last element from the dequeue but does not remove it."""
        if self.count == 0:
            raise Empty("Dequeue is empty")
        return self._data[-1]
