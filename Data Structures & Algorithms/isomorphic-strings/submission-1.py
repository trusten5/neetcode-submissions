class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen={}
        if len(s) != len(t):
            return False

        for l in range(len(s)):
            print(s[l], t[l])
            if s[l] in seen:
                print(seen[s[l]])
                if t[l] != seen[s[l]]:
                    return False
            seen[s[l]]=t[l]

        seenl=[]
        for k, v in seen.items():
            if v in seenl:
                return False
            else:
                seenl.append(v)

        return True
        
