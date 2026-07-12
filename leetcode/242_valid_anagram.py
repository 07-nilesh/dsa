from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S=Counter(s)
        T=Counter(t)
        if S==T:
            return True

        
s="anagram"
t="nagaram"
sol=Solution()
print(sol.isAnagram(s,t))