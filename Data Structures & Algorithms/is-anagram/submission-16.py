class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        s2={}

        for l in s:
            if l in s1:
                s1[l]+=1
            else:
                s1[l]=1

        for l in t:
            if l in s2:
                s2[l]+=1
            else:
                s2[l]=1

        return s1==s2