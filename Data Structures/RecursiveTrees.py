from __future__ import annotations
from typing import Optional, Any, List


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.
    """
    # === Private Attributes ===
    # The item stored at this tree's root, or None if the tree is empty.
    _root: Optional[Any]
    # The list of all subtrees of this tree.
    _subtrees: List[Tree]

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty Tree.
    #
    #   Note: self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   node.

    def swap_down(self) -> None:
        """Swap the root of this Tree with the largest of its children until
        the original root's value is at a position where it's larger than or
        equal to all of its children.

        In the case of a tie, swap with the one that comes first in _subtrees.

        >>> t = Tree(1, [])
        >>> t.swap_down()
        >>> print(t)
        1
        >>> t._subtrees = [Tree(2, []), Tree(3, [])]
        >>> print(t)
        1
          2
          3
        >>> t.swap_down()
        >>> print(t)
        3
          2
          1
        >>> t_large = Tree(3, [Tree(5, [Tree(7, [Tree(2, []), Tree(1, [])])]), \
                               Tree(4, [])])
        >>> print(t_large)
        3
          5
            7
              2
              1
          4
        >>> t_large.swap_down()
        >>> print(t_large)
        5
          7
            3
              2
              1
          4
        """
        if self.is_empty():
            return
        elif self._subtrees == []:
            return
        subtrees = []
        for subtree in self._subtrees:
            if subtree._root is not None:
                subtrees.append(subtree._root)
        root = self._root
        if subtrees != []:
            if self._root < max(subtrees):
                self._root = max(subtrees)
            for subtree in self._subtrees:
                if subtree._root == max(subtrees):
                    subtree._root = root
                    subtree.swap_down()

    # Below are helper methods that we've defined for you.
    # You'll likely want to use this in swap_down.
    def get_root(self) -> Any:
        """Return the value at the root of this Tree.

        >>> t = Tree(1, [])
        >>> t.get_root()
        1
        """
        return self._root

    def set_root(self, value: Any) -> None:
        """Set the value of the _root of this Tree to value.

        >>> t = Tree(1, [])
        >>> t.set_root(2)
        >>> t._root
        2
        """
        self._root = value

    ############################################################################
    # The below are methods given to you. Do NOT change these.
    ############################################################################
    def __init__(self, root: Any, subtrees: List[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return True if this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __str__(self) -> str:
        """Return a string representation of this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        You may find this method helpful for debugging.
        """
        return self._str_indented().strip()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={'disable': ['E1136']})
