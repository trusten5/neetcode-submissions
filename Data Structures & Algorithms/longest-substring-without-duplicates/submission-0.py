class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        slen = 0
        map1={}
        for j in range(len(s)):
            if s[j] in map1:
                i=max(map1[s[j]]+1,i)
            map1[s[j]] = j
            slen = max(slen, j-i+1)


        return slen
            