class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        clean = s.lower()
        for c in clean:
            if c.isalnum():
                new=new+c
        
        return new == new[::-1]