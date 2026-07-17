class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map1={}
        i = 0
        j = 0
        res = 0
        while j<len(s):
            if s[j] in map1:
                i=max(map1[s[j]]+1, i)
                
            map1[s[j]]=j
            res = max(res, j-i+1)
            j+=1
        return res
