from collections import Counter
def isAnagram(s,t):
    if Counter(s)==Counter(t):
        return True
    else:
        return False
print(isAnagram("listen","silent"))
