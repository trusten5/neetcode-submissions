class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        change = {']':'[',')':'(', '}':'{'}

        for c in s:
            if c in change:
                if stack and change[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack