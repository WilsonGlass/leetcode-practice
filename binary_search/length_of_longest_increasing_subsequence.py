"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """
    This solution is interesting because the sub index is not the actual longest increasing subsequence
    It is just that it must stay the same length as the LIS, which is what we want

    e.g.
    [2, 6, 3, 4, 1, 7, 5, 8]
    x | Action | sub
    2 | append | [2]
    6 | append | [2, 6]
    3 | replace 6 | [2, 3]
    4 | append | [2, 3, 4]
    1 | replace 2 | [1, 3, 4]
    7 | append | [1, 3, 4, 7]
    5 | replace 7 | [1, 3, 4, 5]
    8 | append | [1, 3, 4, 5, 8]
    """
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            idx = bisect_left(sub, x)  # Find the index of the first element >= x
            sub[idx] = x  # Replace that number with x
    return len(sub)

def get_longest_increasing_subsequence(nums: List[int]) -> int:
    sub = []
    sub_index = [] # Store index instead of value for tracing path purpose
    trace = [-1] * len(nums) # trace[i] point to the index of previous numer in LIS
    for i, val in enumerate(nums):
        if len(sub) == 0 or sub[-1] < val:
