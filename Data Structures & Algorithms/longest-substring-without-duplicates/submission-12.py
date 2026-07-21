class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        length=0
        i=0

        for n in range(len(s)):
            if s[n] in seen:
                i=max(seen[s[n]]+1, i)
            seen[s[n]]=n
            length=max(length, n-i+1)

        return length

    