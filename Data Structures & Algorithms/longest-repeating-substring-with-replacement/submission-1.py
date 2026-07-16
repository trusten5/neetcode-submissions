class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cset = set(s)
        
        for current in cset:
            count = 0
            l = 0

            for r in range(len(s)):

                if s[r] == current:
                    count+=1
                
                while (r - l + 1) - count > k:
                    if s[l] == current:
                        count-=1
                    l+=1
                res = max(res, r-l+1)
        return res
                

            
