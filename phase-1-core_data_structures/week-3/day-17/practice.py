import heapq
def sortedSquares(nums):
    sqr=[nums[x]**2 for x in range(len(nums))]
    heapq.heapify(sqr)
    sqr.sort()
    return sqr
print(sortedSquares([-4,-1,0,3,10]))

def sortedSquares1(nums):
    result=[0]*len(nums)
    write_dx=len(nums)-1
    left,right=0,len(nums)-1
    while left<= right:
        left_sqr=nums[left]**2
        right_sqr=nums[right]**2
        if left_sqr>right_sqr:
            result[write_dx]=left_sqr
            left+=1
        else:
            result[write_dx]=right_sqr
            right-=1
        write_dx-=1
    return result
print(sortedSquares1([-4,-1,0,3,10]))