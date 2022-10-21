from Tree import Tree

class LinkedTree(Tree):
    """Linked representation of a general tree structure."""

    #-------------------------- Nested _Node class --------------------------
    class _Node:
        __slots__ = '_element', '_parent', '_children'
        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = [children]

        #---------------------------- internal class for positions ----------------------------
    class Position(Tree.Position):
        """An abstracton representing the location of a single element."""
        
        def __init__(self, container, node):
            """Contructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Returns the element at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Returns True if other is a Position."""
            return  type(other) is type(self) and other._node is self._node

    #---------------------------- private methods for node and position relations ----------------------------
    def _validate(self, p):
        """Return associated node if it is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is not p._node:          # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node."""
        return self.Position(self, node) if node is not None else None

    #---------------------------- Linked tree constructor ----------------------------
    def __init__(self):
        """Create an initially empty linked tree."""
        self._root = None
        self._size = 0

    #---------------------------- public accessors ----------------------------
    def __len__(self):
        return self._size

    def root(self):
        """Return the root Position of the tree."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def siblings(self, p):
        """Return a list of positions representing p's siblings or (None if no siblings)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            return parent._node._children

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for cp in node._children:
            child = self._validate(cp)
            yield child

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._children)

    #---------------------------- private accessors ----------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position."""
        if self._root is not None: raise ValueError('Root exists')
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_child(self, p, e):
        """Create a new child for Position p, storing element e, and returns the Position of the new node."""
        node = self._validate(p)
        self._size += 1
        child = self._Node(e, node)
        node._children += child
        return self._make_position(child)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return the old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, replacing it with its child where possible, and returning the element at Position p."""
        node = self._validate(p)
        for cp in node._children:
            child = self._validate(cp)
            child._parent = node._parent
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t):
        """Attach tree t as subtree of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t):
            raise TypeError('Tree types must match')
        self._size += len(t)
        if not t.is_empty():
            t._root._parent = node
            node._children += t._root
            t._root = None
            t._size = 0

