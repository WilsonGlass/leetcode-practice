def find_min_rotated(nums: list[int]) -> int:
    """
    A sorted array of unique integers was rotated at an unknown pivot.
    For example: [10, 20, 30, 40, 50] -> [30, 40, 50, 10, 20]

    input: [30, 40, 50, 10, 20] -> output 3, because the smallest element is 10 and its index is 3
    input: [3, 5, 7, 11, 13, 17, 19, 21, 2] -> output 7, because the smallest element is 2, and its index is 7
    :param arr:
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]