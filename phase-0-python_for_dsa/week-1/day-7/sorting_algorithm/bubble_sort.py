def bubbleSort(nums:list[int]):
    n=len(nums)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if not swapped:
            break     
    return nums
print(bubbleSort([5, 1, 4, 2]))

"""⏱️ Complexity Analysis:
Worst Case Time: O(N^2) (When the array is reversed)
Best Case Time (with optimization): O(N) (When the array is already sorted, it breaks after 1 pass!)
Space Complexity: O(1) (In-place sorting, no extra memory used)"""