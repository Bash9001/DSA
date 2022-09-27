from queue import Empty, Full
from _Array import _Array

class Stack(_Array):
    """Stack data type using an array. An integer value must be provided to assign the size of the array."""
 
    def push(self, x):
        """Adds x to the top of the Stack. Raises an exception if the Stack is full."""
        if self._count == self._size:
            raise Full("Stack is full.")
        self._data[self._count] = x
        self._count += 1

    def pop(self):
        """Removes and returns the top element at the top of the Stack. Raises an exception if the Stack is empty."""
        if self._count == 0:
            raise Empty("Stack is empty.")
        result = self._data[self._count-1]
        self._data[self._count-1] = None
        self._count -= 1
        return result


    def top(self):
        """Returns the top element from the Stack but does not remove it. Raises and exception if the Stack is empty."""
        if self._count == 0:
            raise Empty("Stack is empty")
        return self._data[self._count-1]
