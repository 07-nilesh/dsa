def partition(nums,low,high):
    pivot=nums[high]
    i=low-1
    for j in range(low,high):
        if nums[j]<=pivot:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    nums[i+1],nums[high]=nums[high],nums[i+1]
    return i+1
def quick_sort(nums,low,high):
    if low<high:
        pi=partition(nums,low,high)
        quick_sort(nums,low,pi-1)
        quick_sort(nums,pi+1,high)

data=[5,1,4,3,2]
quick_sort(data,0,len(data)-1)
print(data)

"""
⏱️ Complexity Analysis
-> Best/Average Case Time: O(N log N) — This happens if your pivot splits the array roughly in half every single time.
-> Worst Case Time: O(N^2) — This happens if the array is already sorted (or reversed) 
   and you always pick the first or last element as your pivot.You end up splitting arrays 
   into 0 elements on one side and N-1 elements on the other side,turning your tree into a long linear loop.
"""