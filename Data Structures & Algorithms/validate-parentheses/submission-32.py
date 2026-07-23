class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        change = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char in change:
                if stack and stack[-1]==change[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack