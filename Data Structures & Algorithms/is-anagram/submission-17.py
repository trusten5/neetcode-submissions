class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1, seen2 = {}, {}

        for n in s:
            if n in seen1:
                seen1[n]+=1
            else:
                seen1[n]=1
        
        for n in t:
            if n in seen2:
                seen2[n]+=1
            else:
                seen2[n]=1

        return seen1==seen2