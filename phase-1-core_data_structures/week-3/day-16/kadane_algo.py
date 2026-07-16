def max_subarray(nums):
    max_sum=current_sum=nums[0]
    for num in nums:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([-5,-2,-4]))

# Time: O(n) | Space: O(1)