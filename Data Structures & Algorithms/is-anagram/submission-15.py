class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1={}
        set2={}

        for l in s:
            if l in set1:
                set1[l]+=1
            else:
                set1[l]=1
        
        for l in t:
            if l in set2:
                set2[l]+=1
            else:
                set2[l]=1
        
        return set1==set2
