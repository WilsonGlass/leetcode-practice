"""
Given an integer array nums, return the length of the longest
strictly increasing subsequence

E.g.
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Because of [2, 3, 7, 101]
"""

def length_of_increasing_subsequence(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)