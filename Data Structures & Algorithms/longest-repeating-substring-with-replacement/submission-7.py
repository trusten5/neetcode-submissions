class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        length = 0

        for c in chars:
            count = 0
            t=0
            for l in range(len(s)):
                if s[l]==c:
                    count+=1
                while (l-t+1) - count > k:
                    if s[t]==c:
                        count-=1
                    t+=1
                length = max(length, l-t+1)

        return length
