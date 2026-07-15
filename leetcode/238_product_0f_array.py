def product(nums):
    if len(nums)<2:
        return nums
    
    prefix=[1]*len(nums)
    run_product=1
    for i in range(len(nums)):
        prefix[i]=run_product
        run_product*=nums[i]
    run_sufix=1
    for j in range(len(nums)-1,-1,-1):
        prefix[j]*=run_sufix
        run_sufix*=nums[j]
    return prefix
     
        
print(product([1,2,3,4]))
    