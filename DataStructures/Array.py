"""Array data type using the Python list."""

class Array:
    """Upon initialising the Array, an integer value must be provided to assign the size."""
    def __init__(self, size: int):
        self.size = size
        self._data = [None]*self.size

    def max_len(self):
        """Returns the size of the Array."""
        return self.size