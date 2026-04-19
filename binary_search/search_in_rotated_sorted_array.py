def search(nums: list[int], target: int) -> int:
    """
    At any point during the search in the rotated array, one half will always
    be sorted. Determining which half is sorted is crucial for our modified binary search

    If left half is sorted: We know this if the element at low is less than or equal to
    the element at mid. In a normally sorted array, if the start is less than or equal to
    the mid point, it means all elements till the midpoint are in the correct increasing order

    If right half is sorted: This is the else part. If the left half isn't sorted, the right
    half must be. The target lies within this sorted right half.
        If the target lies within this sorted right half we know the target is greater than the element
        at mid and less than or equal to the element at high

    Rationale:
        The beauty of this approach lies in its ability to determine with certainty
        which half of the array to look in, even though the array is rotated. By checking which half
        of the array is sorted and then using the sorted property to determine if
        the target lies in that half, we can efficiently eliminate half of the array from
        consideration at each step.
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1