def productExceptSelf(nums):
    n=len(nums)
    result=[1]*n

    running_product=1
    for i in range(n):
        result[i]=running_product
        running_product*=nums[i]
    running_product=1
    for i in range(n-1,-1,-1):
        result[i]*=running_product
        running_product*=nums[i]
    return result
print(productExceptSelf([1,2,3,4]))