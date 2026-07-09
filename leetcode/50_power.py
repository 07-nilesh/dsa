class Solution:
    def myPow(self,x,n):
        if n==0:
            return 1
        elif n<0:
            return 1 /self.myPow(x,-n)
        elif n%2==0:
            half =self.myPow(x,n//2)
            return half*half
        return x*self.myPow(x,n-1)
    
print(Solution().myPow(3,3))