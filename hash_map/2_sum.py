def two_sum(arr: list[int], target: int) -> list[int]:
    """
    Iterate through the array only once. At each iteration, check to see the other values that have already been
    stored in our dictionary with their corresponding index. Find the difference between the target and the current
    value, and see if the complement already exists in the dictionary. If so, return the correct indices.
    :param arr:
    :param target:
    :return:
    """
    num_to_index = {}

    for i, val in enumerate(arr):
        complement = target - val
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[val] = i
    return []