def merge(left,right):
    result=[]
    i=0
    j=0
    while i< len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else :
            result.append(left[i])
            i+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(nums):
    if len(nums)<=1:
        return nums
    else:
        mid=len(nums)//2
        left=mergeSort(nums[:mid])
        right=mergeSort(nums[mid:])
        return merge(left,right)
print(mergeSort([5,1,4,2]))

"""
⏱️ Complexity Analysis
Worst Case Time: O(N log N) (Splitting takes $\log N$ levels, and merging at each level takes $O(N)$ operations).
Best Case Time: O(N log N) (Even if it's already sorted, it must split and recombine completely).
Space Complexity: O(N) (Because slicing creates brand-new lists in memory during splitting, and the result array stores elements during merging).

"""

