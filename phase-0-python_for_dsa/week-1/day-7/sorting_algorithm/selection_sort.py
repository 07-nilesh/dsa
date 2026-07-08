def selectionSort(nums:list[int]):
    n=len(nums)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if nums[min_idx]>nums[j]:
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]
    return nums
print(selectionSort([5,1,4,2]))
"""
⏱️ Complexity Analysis
Worst Case Time: O(N^2) (Nested loops scanning the remaining unsorted array)
Best Case Time: O(N^2) (Even if the array is sorted, the inner loop still scans to verify the minimum)
Space Complexity: O(1) (In-place sorting, no extra memory used)
"""