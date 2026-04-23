"""
Given a binary search tree, find the lowest common ancestor
node of two given nodes in the binary search tree

According to the definition of lowest common ancestor:
"The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant
of itself)."
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        left = None
        right = None

def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val > root.val and q.val > root.val:
            # If p and q > root, go right
            root = root.right
        elif p.val < root.val and q.val < root.val:
            # If p and q < root, go left
            root = root.left
        else:
            # Otherwise, must be lowest common ancestor
            return root