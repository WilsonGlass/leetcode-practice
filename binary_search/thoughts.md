We obviously know what binary search is, but to help ourselves remember how to write it in code here is the general format:

```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

What types of problems will typically require binary search?
* Find the first true in a sorted boolean array
* Find the minimum in a rotated sorted array