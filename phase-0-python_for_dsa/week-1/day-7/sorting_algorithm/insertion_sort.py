def insertionSort(nums: list[int]):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
print(insertionSort([5,1,4,2]))

"""
⏱️ Complexity Analysis
Worst Case Time: O(N^2) (When the array is in reverse order)
Best Case Time: O(N) (When the array is already sorted—the while loop never executes!)
Space Complexity: O(1) (In-place sorting)
"""