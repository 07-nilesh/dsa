class Solution:
    def isValid( s: str) -> bool:

        stack=[]
        close_to_open={'}':'{',']':'[',')':'('}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack:
                    if close_to_open[char]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(stack)==0 
print(Solution.isValid("(]"))
print(Solution.isValid("()"))
print(Solution.isValid("([])"))