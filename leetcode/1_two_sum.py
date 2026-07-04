
nums=[2,7,11,15]
target=9
def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
            else:
                j=j+1
     


def sum_two(nums,target):
    num_dict={}
    current_nums=0
    for i in range(len(nums)):
        
        current_nums=nums[i]
        partner=target-current_nums
        
        if partner in num_dict:
            return i,num_dict[partner]
        else:
            num_dict[current_nums] = i
        

        
        
        
        
        
print(sum_two(nums, target))
print(sum_two([3,2,4],target=6))
