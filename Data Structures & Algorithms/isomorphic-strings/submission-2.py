class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seens, seent = {},{}
        if len(s) != len(t):
            return False

        for l in range(len(s)):
            if s[l] in seens:
                if t[l] != seens[s[l]]:
                    return False
            seens[s[l]]=t[l]
            if t[l] in seent:
                if s[l] != seent[t[l]]:
                    return False
            seent[t[l]]=s[l]


        return True
        
