class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i < j:
            print(i, j, s.lower())
            if i < j and not s.lower()[j].isalnum():
                j-=1
            elif i < j and not s.lower()[i].isalnum():
                i+=1
            elif s.lower()[i] != s.lower()[j]:
                return False
            else:
                i+=1
                j-=1
        
        return True