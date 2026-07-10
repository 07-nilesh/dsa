class Solution:
    def maxArea(height:list[int])->int:
        maxArea=0
        left,right=0,len(height)-1
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if area>=maxArea:
                maxArea=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
print(Solution.maxArea([2,7,11,15]))