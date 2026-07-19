def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged=[intervals[0]]

    for current_start,current_end in intervals[1:]:
        last_merged_start,last_merged_end=merged[-1]

        if current_start<=last_merged_end:
            merged[-1][1]=max(last_merged_end,current_end)
        else:
            merged.append([current_start,current_end])
    return merged
test_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(test_input))
print(merge_intervals([[4, 5], [1, 4]]))
# TC : O(nlogn)