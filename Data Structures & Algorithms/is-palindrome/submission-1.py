class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = [x for x in s.lower() if x.isalnum()]
        print(li)
        print(li[::-1])
        return li == li[::-1]