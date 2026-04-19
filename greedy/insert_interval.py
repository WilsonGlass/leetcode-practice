"""
You are given an array of non-overlapping intervals
_intervals_ where intervals[i] = [start_i, end_i] represents the start and the end of
the ith interval and intervals is sorted in ascending order by start_i. You are also
given an interval of new_interval = [start, end] that represents the start and end of
another interval

Insert new_interval into intervals s.t. intervals is still sorted in ascending order by start_i and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion

Note: You don't need to modify intervals in-place. You can make a new array and return it.
"""

def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    res = []

    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            # greedy
            end = max(end, intervals[i][1])
        else:
            res.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    res.append([start, end])
    return res