class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for l in t:
            if i< len(s) and l == s[i]:
                i+=1

        return i==len(s)