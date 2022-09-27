from queue import Empty


class SinglyLinkedList:
    """Singly linked list made up of individual nodes, each comprising of an element and pointer for the next node."""

    #-----------------------------Nested _Node class-----------------------------
    class _Node:
        """Nonpublic class for indivual nodes in a linked list."""
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    #-----------------------------Linked List methods-----------------------------
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the list."""
        return self._size

    def __iter__(self):             # Custom iterator method to iterate from on node to the next
        pointer = self.head
        while pointer is not None:
            yield pointer
            pointer = pointer.next

    def is_empty(self):
        """Returns True if the list is empty."""
        return self._size == 0

    def traverse(self):
        """Returns a list of every nodes' elements in the linked list."""
        answer = []
        for Node in self:
            answer.append(Node.element)
        return answer

    def add_first(self, e):
        """Extend the linked list from the head."""
        new = self._Node(e, self.head)
        self.head = new
        self._size += 1
        if self._size == 1: self.tail = self.head

    def add_last(self, e):
        """Extend the linked list from the tail."""
        new = self._Node(e, None)
        self.tail.next = new
        self.tail = new
        self._size += 1
        if self._size == 1: self.head = self.tail

    def remove_first(self):
        """Removes and returns the current head of the linked list."""
        if self.head == None:
            raise Empty("List is empty.")
        answer = self.head.element
        self.head = self.head.next
        self._size -= 1
        return answer
