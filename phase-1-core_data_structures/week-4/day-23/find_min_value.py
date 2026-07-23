def min_element(nums):
    left,right=0,len(nums)-1
    while left < right :
        mid = left + (right-left)//2
        if nums[mid] > nums[right]:
            left=left+1
        else:
            right=mid
    return nums[left]
print(min_element([4,5,6,7,0,1,2]))