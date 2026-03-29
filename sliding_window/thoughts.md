<b>Sliding Window</b>

Fixed Window:

* "Find the maximum average of any subarray of size k"
* "Return the sum of every k-length block"
* "Find the subarray of length k with the largest/smallest X"

```python
def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans
```

Dynamic Window:

Used for finding the optimal window size such that some
condition is met

* "Find the length of the longest substring with at most K unique characters"
* "What's the smallest subarray with a sum greater than a target"
* "Return the longest window where a certain rule is valid"

You expand on the right until a certain metric is violated, then retract one index on the left and repeat.

```python
def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window 
        while invalid(window):
            remove input[left] from window
        ans = max(ans, window)
    return ans
```