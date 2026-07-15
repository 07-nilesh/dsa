class Solution:
    def findduplicate(nums: list[int]) -> bool:
        unique=set(nums)
        if len(unique)==len(nums):
            return False
        else:
            return True
print(Solution.findduplicate(nums=[1,2,3,1]))
print(Solution.findduplicate(nums=[1,2,3,4]))

