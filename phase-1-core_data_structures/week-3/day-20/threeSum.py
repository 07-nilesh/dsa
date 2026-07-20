def threeSum(nums):
    nums.sort()
    n=len(nums)
    result=[]

    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left,right=i+1,n-1
        while left < right :
            total=nums[i]+nums[left]+nums[right]

            if total==0:
                result.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif total <0:
                left+=1
            else:
                right-=1
    return result
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-1, 0, 0, 1, 1]))
print(threeSum([0,0,0,0,0,0]))

'''
TC : O(n^2)  | space : O(1) or O(n)
REBUILD
def threesum(nums):
    nums.sort()
    n=len(nums)
    result=[]

    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,n-1
        while l<r :
            target=nums[i]+nums[l]+nums[r]
            if target==0:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif target<0:
                l+=1
            else:
                r-=1
    return result
print(threesum([-1, 0, 1, 2, -1, -4]))
'''