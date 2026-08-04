class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cset=set(s)
        max_c=0

        for c in cset:
            l=0
            count = 0

            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                while (r-l+1) - count > k:
                    if s[l]==c:
                        count-=1
                    l+=1
                max_c = max(max_c, r-l+1)

        return max_c

