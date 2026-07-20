class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        j=0

        count=0

        for l in range(len(s)):
            if s[l] in seen:
                j=max(seen[s[l]]+1, j)
            seen[s[l]]=l
            count=max(count, l-j+1)

        return count