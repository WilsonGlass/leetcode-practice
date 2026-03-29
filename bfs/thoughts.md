<b>BFS</b>

Recall that for BFS we use a queue, first in first out

```python
def tree_bfs(root):
    queue = deque([root])
    while len(queue):
        node = queue.popleft()
        for child in node.children:
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND
```

Useful for:
* Traversing a tree from top to bottom
* Care about depth, distance, or levels
* Looking for the first match/closest node to root

```python
def graph_bfs(root):
    queue = deque([root])
    visited = set([root])
    while len(queue):
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
```

Useful for:
* Working with grids, adjacency lists, or networks
* Structure can contain cycles or duplicate paths
* Need to find the shortest number of steps
* Exploring possible states

In General BFS follows this pattern:
1. A queue for the current layer of exploration
2. A loop to process each node
3. A branching step where nodes are added to the queue