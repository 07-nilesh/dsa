def twoSum(nums,target):
    unique={}
    for i in range(len(nums)):
        
        curent_sum=nums[i]
        partner=target-curent_sum
        if partner in unique:
            return unique[partner],i
        else:
            unique[curent_sum]=i

        