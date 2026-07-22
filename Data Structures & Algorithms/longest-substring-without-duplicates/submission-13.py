class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        j=0
        count = 0
        for i in range(len(s)):
            if s[i] in seen:
                j=max(j, seen[s[i]]+1)
            seen[s[i]]=i
            count = max(count, i-j+1)

        return count
