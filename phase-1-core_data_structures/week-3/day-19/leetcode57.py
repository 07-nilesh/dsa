'''
class Solution:
    def insert( intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged=[intervals[0]]

        for start,end in intervals[1:]:
            merge_start,merge_end=merged[-1]
            if start <= merge_end:
                merged[-1][1]=max(merge_end,end)
            else:
                merged.append([start,end])
        return merged


print(Solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))

'''

class Solution:
    def insert( intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        merged=[]
        n=len(intervals)
        i=0
        while i<n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        merged.append(newInterval)
        while i < len(intervals):
            merged.append(intervals[i])
            i+=1
        return merged


print(Solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))

# Tc : O(n) | space : O(n)