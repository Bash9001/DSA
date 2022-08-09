"""Stack data type using an array."""

from Array import Array

class Stack(Array):
    """Upon initialising the Stack, an integer value must be provided to assign the size of the array."""
    def __init__(self, size: int):
        Array.__init__(self, size)
        self.count = 0

    def __len__(self):
        """Returns the length of the Stack."""
        return self.count

    def is_empty(self):
        """Returns True if the Stack is empty and False if it has contents."""
        return self.count == 0

    def is_full(self):
        """Returns True if the Stack Array is full and False if it has space."""
        return self.count == self.size

    def push(self, x):
        """Adds x to the top of the Stack. Raises an exception if the Stack is full."""
        if self.count == self.size:
            raise IndexError("Stack is full.")
        self._data[self.count] = x
        self.count += 1

    def pop(self):
        """Removes and returns the top element at the top of the Stack. Raises an exception if the Stack is empty."""
        if self.count == 0:
            raise IndexError("Stack is empty.")
        result = self._data[self.count-1]
        self._data[self.count-1] = None
        self.count -= 1
        return result


    def top(self):
        """Returns the top element from the Stack but does not remove it. Raises and exception if the Stack is empty."""
        if self.count == 0:
            raise AttributeError("Stack is empty")
        return self._data[self.count-1]
