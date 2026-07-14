class Solution:
    def isPalindrome(self, s: str) -> bool:
        back = len(list(s))-1
        front=0


        while front<back:
            while front < back and not s[front].isalnum():
                front+=1
            while front < back and not s[back].isalnum():
                back-=1
            if s[front].lower()!=s[back].lower():
                return False
            front+=1
            back-=1
        return True