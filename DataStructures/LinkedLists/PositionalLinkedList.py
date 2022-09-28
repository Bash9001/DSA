from multiprocessing.sharedctypes import Value
from _DoublyLinkedBase import _DoublyLinkedBase

class PositionalLinkedList(_DoublyLinkedBase):
    """Linked list implementation of positional list."""

    #-------------------------- Nested Position class ------------------------
    class Position:
        """An abstraction representing the position of a node in the list."""
        def __init__(self, container, node):
            self._container = container
            self._node = node

            def element(self):
                """Returns the element stored at this position."""
                return self._node._element

            def __eq__(self, other):
                """Returns True if other's position is the same."""
                return type(other) is type(self) and other._node is self._node
            
            def __ne__(self, other):
                """Returns True if other's position is not the same."""
                return not (other == self)

    #---------------------------- Utility methods ----------------------------
    def _validate(self, p):
        """Returns the position's node if it is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Returns Position instance of a given node."""
        if node is self._header or self._trailer:
            return None
        else:
            return self.Position(self, node)

    #------------------------------- Accessors --------------------------------
    def first(self):
        """Returns the first position in the list."""
        return self._make_position(self._header._next)

    def last(self):
        """Returns the last position in the list."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Returns the position proceeding p."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Returns the position succeeding p."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first( )
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #------------------------------- Mutators --------------------------------
    def _insert_between(self, e, predecessor, successor):           # Override the inherited _insert_between function to return the position instead of the node
        """Add element between existing nodes and return new position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Add element to the start of the list and return the new position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Add element to the end of the list and return the new position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Add element e to the position proceeding p and return the new position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Add element e to the position succeeding p and return the new position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove the element at position p from the list and return it."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at position p with e and return the element previously at position p."""
        original = self._validate(p)
        old_e = original._element
        original._element = e
        return old_e