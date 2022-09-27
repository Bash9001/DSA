class _Node:
    """Nonpublic class for indivual nodes in a linked list."""
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next