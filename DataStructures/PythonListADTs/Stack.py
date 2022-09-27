from queue import Empty


class Stack:
    """Stack data type using a list."""
    def __init__(self):
        self._data = []

    def __len__(self):
        """Returns the length of the Stack."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the Stack is empty."""
        return len(self._data) == 0

    def push(self, x):
        """Adds x to the top of the Stack."""
        self._data.append(x)

    def pop(self):
        """Removes and returns the top element at the top of the Stack."""
        if len(self._data) == 0:
            raise Empty("Stack is empty.")
        return self._data.pop()

    def top(self):
        """Returns the top element from the Stack but does not remove it."""
        if len(self._data) == 0:
            raise Empty("Stack is empty")
        return self._data[-1]
