class Solution:
    def isValid(self, s: str) -> bool:
        last=['']
        for t in s:
            if t=='(' or t=='{' or t=='[':
                last.append(t)
            elif (last[-1]=='(' and t==')') or (last[-1]=='{' and t=='}') or (last[-1]=='[' and t==']'):
                last=last[:len(last)-1]
            else:
                return False

        return len(last)<2
                
