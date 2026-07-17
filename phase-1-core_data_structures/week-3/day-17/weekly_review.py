def two_sum(nums,target):
    num_dict={}
    
    for i in range(len(nums)):
        current_sum=nums[i]
        partner=target-current_sum
        if partner in num_dict:
            return i, num_dict[partner]
        num_dict[current_sum]=i

print(two_sum([2,7,11,15],9))