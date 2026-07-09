def is_sorted(nums):
    n=len(nums)
    if n<=1:
        return True
    if nums[0]>nums[1]:
        return False
    return is_sorted(nums[1:])
    
print(is_sorted([5,1,4,2]))
print(is_sorted([1,2,3,4,5]))