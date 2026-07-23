def search(nums,target):
    left,right=0,len(nums)-1
    while left <= right :
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>nums[left]:
            if target<nums[left] or target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        else:
            if target<nums[mid] or target>nums[right]:
                right=mid-1
            else:
                left=mid+1
    return -1
print(search([4,5,6,7,0,1,2,3],0))

'''
TC : O(logn) | space : O(1)
def search(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        m=l+(r-l)//2
        if m==target:
            return m
        if nums[m]>=nums[l]:
            if target>nums[m] or target<nums[l]:
                l=m+1
            else:
                r=m-1
        else:
            if target<nums[m] or target>nums[r]:
                r=m-1
            else:
                l=m+1
    return -1
    '''