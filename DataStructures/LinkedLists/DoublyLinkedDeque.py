from queue import Empty
from _DoublyLinkedBase import _DoublyLinkedBase

class DoublyLinkedDeque(_DoublyLinkedBase):
    """Linked list implementation of a deque."""
    
    def first(self):
        """Returns the first element in the deque."""
        if self.is_empty(): raise Empty("Deque is empty.")
        return self._header._next._element

    def last(self):
        """Returns the last element in the deque."""
        if self.is_empty(): raise Empty("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Inserts an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Inserts and element to the end of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Removes and returns the first element of the deque."""
        if self.is_empty(): raise Empty("Deque is empty.")
        self._delete_node(self._header._next)

    def delete_last(self):
        """Removes and returns the last element of the deque."""
        if self.is_empty(): raise Empty("Deque is empty.")
        self._delete_node(self._trailer._prev)