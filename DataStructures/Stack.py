"""Stack data type using a list."""

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        """Returns the length of the Stack."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the Stack is empty and False if it has contents."""
        return len(self._data) == 0

    def push(self, x):
        """Adds x to the top of the Stack."""
        self._data.append(x)

    def pop(self):
        """Removes and returns the top element at the top of the Stack. Raises an exception if the Stack is empty."""
        if len(self._data) == 0:
            raise IndexError("Stack is empty.")
        return self._data.pop()

    def top(self):
        """Returns the top element from the Stack but does not remove it. Raises and exception if the Stack is empty."""
        if len(self._data) == 0:
            raise AttributeError("Stack is empty")
        return self._data[-1]
