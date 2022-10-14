class Tree:
    """Abstract base class representing a tree structure."""

    #---------------------------- nested Position class ----------------------------
    class Position:
        """Abstract child class representing the location of an element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """Return True if other position returns the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self==other)

    
    #---------------------------- abstract methods to be supported by concrete subclass ----------------------------
    def root(self):
        """Return Position representing the tree's root."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return the Position representing p's parent."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children of p."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Iterate through the positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    #---------------------------- concrete methods implemented in this class ----------------------------
    def is_root(self, p):
        """Returns True if position p represents the tree's root."""
        return self.root() == p

    def is_leaf(self, p):
        """Returns True if position p has no children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Returns True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Returns the number of levels seperating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p."""
        if p is None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))