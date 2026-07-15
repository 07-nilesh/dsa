'''
class Solution:
    def pivotIndex( nums: list[int]) -> int:
        prefix=[0]*len(nums)
        running_prefix=0
        for i in range(len(nums)):
            prefix[i]=running_prefix
            running_prefix+=nums[i]
        sufix=[0]*len(nums)
        running_sufix=0
        for j in range(len(nums)-1,-1,-1):
            sufix[j]=running_sufix
            running_sufix+=nums[j]
        for k in range(0,len(nums)-1):
            if prefix[k]==sufix[k]:
                return k
     
        return -1
print(Solution.pivotIndex([1,7,3,6,5,6]))
'''
def pivot(nums):
    total_sum=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        right_sum=total_sum-left_sum-nums[i]
        if left_sum==right_sum:
            return i
        else:
            left_sum+=nums[i]

    return -1
print(pivot([1,7,3,6,5,6]))
    