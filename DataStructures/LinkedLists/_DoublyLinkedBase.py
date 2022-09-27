class _DoublyLinkedBase:
    """Nonpublic doubly linked list made up of individual nodes, each comprising of an element and pointers for the previous and next nodes."""
    
    #-----------------------------Nested _Node class-----------------------------
    class _Node:
        """Nonpublic class for indivual nodes in a linked list."""
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    #-----------------------------Linked List methods-----------------------------
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.next = self._header
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the linked list."""
        return self._size
    
    def is_empty(self):
        """Returns True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Adds a new node between 2 existing nodes in the list and returns the new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete a non-sentinel node from the list and return it's element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return element