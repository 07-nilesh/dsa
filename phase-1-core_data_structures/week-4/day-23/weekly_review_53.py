def max_subarray(nums):
    current_sum=max_sum=nums[0]
    for i in range(1,len(nums)):
        current_sum=max(nums[i],current_sum+nums[i])
        max_sum=max(current_sum,max_sum)
    return max_sum
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

def max_subarray1(nums):
    current_sum=max_sum=nums[0]
    for i in range(1,len(nums)):
        if current_sum<0:
            current_sum=0
        current_sum+=nums[i]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
print(max_subarray1([-2,1,-3,4,-1,2,1,-5,4]))
