def trap(height):
    if not height:
        return 0
    left,right=0,len(height)-1
    max_left=height[left]
    max_right=height[right]
    water_trapped=0

    while left < right :
        
        if max_left < max_right:
            left+=1
            max_left=max(max_left,height[left])
            water_trapped+=max_left-height[left]
        else:
            right-=1
            max_right=max(max_right,height[right])
            water_trapped+=max_right-height[right]
    return water_trapped
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([1, 0, 2, 0, 3]))