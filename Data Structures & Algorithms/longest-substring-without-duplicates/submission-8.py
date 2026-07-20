class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        j=0
        sublen = 0
        for i in range(len(s)):
            print([j, i, s[i]])
            if s[i] in seen:
                j=max(seen[s[i]]+1,j)
            seen[s[i]]= i
            sublen=max(sublen, i-j+1)
        
        return sublen
            
