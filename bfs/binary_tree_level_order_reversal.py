from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    """
    Given a binary tree, return its level order traversal. The input is the root
    node of the tree, the output shouldbe a list of lists of integers, with the ith
    list containing the values of nodes on level i from left to right

    notes because I am awful at trees:
    * You create a queue with just the root in it
    * Create a while loop with the condition of the length of the queue being greater than 0
    * Create a level per iteration of the initial while loop for a new for loop of the length of the current level
    * Remove the left most value and add it to a temporary variable, then append that temporary variable to the new_level list
    * Check the left and right nodes of node.left and node.right, and append to the end of the queue
    * Then add that level to the res and keep iterating until everything has been covered
    :return:
    """
    res = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)