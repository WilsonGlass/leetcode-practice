def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    to_be_removed = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end: # overlap
            to_be_removed += 1
            # don't update prev_end, we're "removing" the current interval
            # keeping the one with the smaller end time which is already prev_end
        else:
            prev_end = intervals[i][1] # no overlap, move forward

    return to_be_removed