class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        change = {']': '[', ')':'(', '}':'{'}

        for b in s:
            if stack:
                if b in change: 
                    if stack[-1]==change[b]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(b)
            else:
                stack.append(b)
        
        return not stack
