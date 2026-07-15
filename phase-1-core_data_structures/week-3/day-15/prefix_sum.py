def build_prefix(nums):
    prefix=[0]*(len(nums)+1)
    for i in range(len(nums)):
        prefix[i+1]=prefix[i]+nums[i]
    return prefix
def range_sum(prefix,left,right):
    return prefix[right+1]-prefix[left]

nums=[1,2,3,4,5]
prefix=build_prefix(nums)
print(prefix)
print(range_sum(prefix,1,3))