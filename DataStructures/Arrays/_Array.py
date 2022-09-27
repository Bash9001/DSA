class _Array:
    """Nonpublic array class with preallocated memory."""
    def __init__(self, size: int):
        self._size = size
        self._data = [None]*self._size
        self._count = 0

    def __iter__(self):                 # Custom iterator method to iterate through all elements in the array
        for i in range(self._count):
            yield self._data[i]

    def __len__(self):
        """Returns the current _size of the array."""
        return self._count
  
    def max_len(self):
        """Returns the allocated max _size of the array."""
        return self._size

    def is_empty(self):
        """Returns True is array is empty."""
        return self._count == 0

    def is_full(self):
        """Returns True if the array is full"""
        return self._count == self._size
