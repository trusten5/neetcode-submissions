class Solution:
    def isValid(self, s: str) -> bool:
        last=['']
        for t in s:
            print(last[-1], t)
            print(last[-1]=='[' and t==']')
            if t=='(' or t=='{' or t=='[':
                last.append(t)
            elif (last[-1]=='(' and t==')') or (last[-1]=='{' and t=='}') or (last[-1]=='[' and t==']'):
                last=last[:len(last)-1]
            else:
                return False
        
        print(len(last)<2)

        return len(last)<2
                
