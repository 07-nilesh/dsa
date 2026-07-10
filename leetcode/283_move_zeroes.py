class Solution:
    def moveZero(nums:list[int])->None:
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        print(nums)
print(Solution.moveZero([0,1,0,3,12]))