class Solution:
    def maxAvg(nums,k):
        if len(nums)<=k:
            return float((sum(nums[:k]))/k)
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum=max(window_sum,max_sum)

        return float(max_sum/k)
print(Solution.maxAvg([13,3,5,7,0],4))