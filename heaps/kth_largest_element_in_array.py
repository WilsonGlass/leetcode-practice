from heapq import heapify, heappop

"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not necessarily the kth distinct element

e.g. [3, 2, 1, 5, 6, 4], k = 2 => Output: 5
e.g. [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 => Output: 4
"""

def find_kth_largest(nums: list[int], k: int) -> int:
    nums = [-x for x in nums] # Because heap is min heap by default, so we need to revert this
    heapify(nums)
    for _ in range(k - 1):
        heappop(nums)
    return -nums[0]

