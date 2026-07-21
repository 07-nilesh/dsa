#1. prefix sum 
def buildprefix(nums):
    n=len(nums)
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+nums[i]
    return prefix
def rangeQuery(prefix,left,right):
    return prefix[right+1] - prefix[left]
nums=[1,2,3,4]
prefix=buildprefix(nums)
print(rangeQuery(prefix,1,3))


# 2. kadanes algorithm 
def kadanes(nums):
    if len(nums)==0:
        return []
    current_sum=max_sum=nums[0]
    for num in nums[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(current_sum,max_sum)
    return max_sum
print(kadanes([1,2,-3,4]))

#3.Merge intervals
def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged=[intervals[0]]

    for current_start,current_end in intervals[1:]:
        last_start,last_end=merged[-1]
        if current_start <= last_end:
            merged[-1][1]=max(last_end,current_end)
        else:
            merged.append([current_start,current_end])
    return merged
print(mergeIntervals([[1,3],[2,5]]))

#4. two pointer for sum
def threeSum(nums):
    nums.sort()
    result=[]

    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            total=nums[i]+nums[l]+nums[r]
            if total ==0:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif total <0:
                l+=1
            else: r-=1
    return result
print(threeSum([-1,0,1,2,0,-2]))

        
