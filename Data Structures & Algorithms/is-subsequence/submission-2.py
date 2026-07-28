class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        if s=="":
            return True
        for l in t:
            if l == s[i]:
                i+=1
                if i == len(s):
                    return True

        return False