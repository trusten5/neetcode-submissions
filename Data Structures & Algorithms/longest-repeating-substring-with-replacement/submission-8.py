class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cset = set(s)
        length = 0

        for c in cset:
            count = 0
            j=0

            for i in range(len(s)):
                if s[i]==c:
                    count +=1

                while (i-j+1) - count > k:
                    if s[j]==c:
                        count-=1
                    j+=1
                
                length = max(length, i-j+1)

        return length