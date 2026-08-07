class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for s in strs:
            key=[0]*26
            for l in s:
                key[ord(l)-ord('a')]+=1
            key=tuple(key)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key]=[s]

        res=[]
        for keys, vals in seen.items():
            res.append(vals)
        
        return res