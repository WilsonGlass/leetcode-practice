"""
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of
the nodes in the tree.


E.g. k = 3 with the tree below:

        3
       / \
      1   4
       \
        2

Go left as far as possible: stack = [3, 1]
Pop 1 -> count = 1, not 3rd yet, move right to node 2.

Go left from 2: stack = [3, 2]
Pop 2 -> count = 2, not 3rd yet, no right child

Stack = [3]
Pop 3 -> count = 3 -> return 3
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_element_in_bst(root: Optional[TreeNode], k: int) -> int:
    count = 0
    stack = []
    curr = root

    while curr or stack:
        # Go as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process this node
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
    return -1 # k was larger than the number of nodes in the tree