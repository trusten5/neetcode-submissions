class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        change = {']': '[', ')':'(', '}':'{'}

        for b in s:
            if b in change:
                if stack and stack[-1]==change[b]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return not stack
