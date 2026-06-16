class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower()
        li = list(clean)
        li = [x for x in li if x.isalnum()==True]
        print(li)
        print(li[::-1])
        return li == li[::-1]