from collections import Counter
import heapq
class Solution:
    def topKFrequent( nums: list[int], k: int) -> list[int]:
        freq=Counter(nums)
        min_heap=[]
        for num,count in freq.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap)>k:
                
                heapq.heappop(min_heap)
            

        return [pair[1] for pair in min_heap]
    

print(Solution.topKFrequent([1,1,1,2,2,3],2))