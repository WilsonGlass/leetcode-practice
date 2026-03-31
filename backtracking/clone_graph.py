class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                # If we've seen this node before then this is a cycle.
                # Don't need to continue just backtrack
                return old_to_new[curr]
            # Create a new node with currs value
            clone = Node(curr.val)

            # Add the new node to the reference dict
            old_to_new[curr] = clone

            for nei in curr.neighbors:
                # Create the new neighbors for the clone
                # This will get populated eventually, but longer paths will have their
                # neighbors populated 1st because this is dfs.
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)
