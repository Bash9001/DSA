from queue import Empty

class Queue:
    """Queue data type using a list."""
    def __init__(self):
        self._data = []

    def __len__(self):
        """Returns the length of the Queue."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the Queue."""
        return len(self._data) == 0

    def enqueue(self, x):
        """Adds x to the end of the Queue."""
        self._data.append(x)
        
    def dequeue(self):
        """Removes and returns the element at the start of the Queue."""
        if len(self._data) == 0:
            raise Empty("Queue is empty.")
        result = self._data[0]
        self._data[0:] = self._data[1:]
        self._data[:-1]
        return result

    def first(self):
        """Returns the first element from the Queue but does not remove it."""
        if len(self._data) == 0:
            raise Empty("Queue is empty")
        return self._data[0]
