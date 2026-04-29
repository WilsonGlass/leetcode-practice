"""
Actual interview question I had.

You are a historian working for a kingdom founded centuries ago by a founding
monarch. As time went on, some of this monarch's children went on to found
their own kingdoms, and so on, so that the history of the kingdoms that came
from this one forms a tree structure.

This kingdom is weirdly revisionist about its history and is willing to totally
cut ties with any other kingdom if its ruler ends up in a scandal or does
anything to damage the collective lineage's reputation. When this happens, the
offending kingdom is removed from the historical record, and any kingdom that
spawned from it is reassigned to its parent (see the example below).

Given an original tree representing the relationships between kingdoms and a list of
kingdoms to strike from the historical record, what is the final height of the
tree?

```
    1              to drop: [3]
   / \
  2   3
      /\
     5  6

Answer: 2
Explanation: After removing kingdom 3, kingdoms 5 and 6 are considered children of 1, and
the final tree drawn below has height 2.

    1
   /|\
  2 5 6
```
"""


class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

def solution(root: TreeNode, node_values_to_be_dropped: list[int]):
    def dfs(node: TreeNode):
        # Base Case
        if not node:
            return 0

        to_be_dropped = node.val in node_values_to_be_dropped
        if not node.children:
            return 0 if to_be_dropped else 1

        # Otherwise
        height = 0
        for child in node.children:
            height = max(dfs(child), height)
        return height if to_be_dropped else height + 1

    return dfs(root)

