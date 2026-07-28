class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        change={'}':'{', ')':'(',']':'['}

        for l in s:
            if l in change:
                if stack and change[l]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)

        return not stack
                