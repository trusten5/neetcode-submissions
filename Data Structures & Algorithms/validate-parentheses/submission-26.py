class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        switch = {']':'[', ')':'(', '}': '{'}

        for n in s:
            if n in switch:
                if stack and switch[n]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        return not stack