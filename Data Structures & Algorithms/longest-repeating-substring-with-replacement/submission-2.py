class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cset=set(s)
        res = 0
        
        for c in cset:
            count = 0

            i=0
            for l in range(len(s)):
                if s[l] == c:
                    count+=1
                while (l-i+1) - count > k:
                    if s[i]==c:
                        count-=1
                    i+=1
                res = max(res, (l-i+1))

        return res
            
                
