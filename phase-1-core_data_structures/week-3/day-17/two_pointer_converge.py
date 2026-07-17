def two_sum_index(nums,target):
    left,right=0,len(nums)-1
    while left <right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return [left+1, right+1]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return []
print(two_sum_index([2,7,11,15],9))
print(two_sum_index([7, 15, 2, 11], 9))

"""
🧠 Time complexity   : O(n) because pointers scan elements at most once without re-scanning.
🧠 Space complexity  : O(1) because only two scalar index trackers are stored regardless of input size."""