<b>backtracking</b>
* Combinations, permutations, etc.
* Building up a partial solution
* Want all possible solutions
* Need to discard bad paths early

```python
ans = []
def dfs(start_index, path, [...additional states]):
    # Base Case
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # Pruny early, important step so we dont go down paths that wont lead anywhere
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()
```

Spot a backtracking problem:
* Generate all combinations or arrangements
* Building up a partial solution
* Want all possible solutions
* Need to discard bad paths early