def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # sort the intervals by their starting time.
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Example Usage:
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1,6],[8,10],[15,18]]

"""
You are given a list of intervals where each interval is a pair of start and end times represented as [start_i, end_i]. Your task is to merge all overlapping intervals and return a list of the merged intervals.

Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Intervals [1, 3] and [2, 6] overlap, so we merge them into [1, 6].

Sorting: We first sort the intervals by their starting time, so the intervals appear in order of when they begin.

for interval in intervals:
This iterates over the sorted list of intervals. Each interval is a pair like [start, end]

if not merged or merged[-1][1] < interval[0]:
This checks two conditions:
not merged: If the merged list is empty, we add the first interval directly because there's nothing to merge yet.
merged[-1][1] < interval[0]: This checks if the current interval overlaps with the last merged interval.
merged[-1][1] is the end time of the last interval in the merged list.
interval[0] is the start time of the current interval.
If the last merged interval’s end time is smaller than the current interval’s start time (merged[-1][1] < interval[0]), it means there is no overlap, and the current interval should be added as a new separate interval.

merged.append(interval)
If the current interval doesn't overlap with the last merged interval (based on the condition above), we add the current interval to the merged list.

else:
If the current interval overlaps with the last merged interval, we move into this block.

merged[-1][1] = max(merged[-1][1], interval[1])
This line updates the end time of the last merged interval to include the current interval.
merged[-1][1] refers to the end time of the last interval in the merged list.
interval[1] refers to the end time of the current interval.
The goal is to merge the overlapping intervals by updating the end time of the last interval to the later of the two end times (max(merged[-1][1], interval[1])).
This ensures that the last merged interval correctly represents the merged span of time for all overlapping intervals.
"""
