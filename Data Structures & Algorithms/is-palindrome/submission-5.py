class Solution:
    def isPalindrome(self, s: str) -> bool:
        back = len(list(s))-1
        front=0


        while front<back:
            while front < back and not s[front].isalpha() and not s[front].isnumeric():
                front+=1
            while front < back and not s[back].isalpha() and not s[back].isnumeric():
                back-=1
            if s[front].lower()!=s[back].lower():
                return False
            front+=1
            back-=1
        return True