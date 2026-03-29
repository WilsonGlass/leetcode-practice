"""
Given an array nums consisting of only non-negative integers,
find the largest sum among all subarrays of length k in nums.
"""

def subarray_sum_fixed(nums: list[int], k: int) -> int:
    max_val = 0
    left = 0
    right = left + k
    while right < len(nums):
        max_val = max(max_val, sum(nums[left:right]))
        left += 1
        right += 1
    return max_val


nums = [1, 2, 3, 7, 4, 1]
k = 3

if __name__ == "__main__":
    nums = [1, 2, 3, 7, 4, 1]
    k = 3
    res = subarray_sum_fixed(nums, k)
    print(res)