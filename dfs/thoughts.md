<b>DFS</b>
* Explore every possibility
* Want to visit all nodes
* Care about structure, not distance

```python
def tree_dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = tree_dfs(root.left, target)
    if left is not None:
        return left
    return tree_dfs(root.right, target)
```

```python
def graph_dfs(root, target):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
```

Graph DFS is useful for
* Puzzles and state exporation
* Graph coloring
* Recursive traversal
* Backtracking