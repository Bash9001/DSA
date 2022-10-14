from Tree import Tree


class BinaryTree(Tree):
    """Abstract base class for a binary tree structure."""

    #---------------------------- additional abstract methods ----------------------------
    def left(self, p):
        """Return a Position representing p's left child."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child."""
        raise NotImplementedError('must be implemented by subclass')

    #---------------------------- additional concrete methods ----------------------------
    def sibling(self, p):
        """Return a Position representing p's sibling or (None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
