"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

e.g.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output = 6
Explanation: [4, -1, 2, 1] has the largest sum 6.
"""

def max_subarray(nums: list[int]) -> int:
    """
    iterate through, check to see if the current sum plus the current index is
    greater than just the current index by itself. Then see if the max sum is greater than the current sum.

    Likely a good thing to remember here.
    """
    max_sum = nums[0]
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(curr_sum, max_sum)
    return max(curr_sum, max_sum)
