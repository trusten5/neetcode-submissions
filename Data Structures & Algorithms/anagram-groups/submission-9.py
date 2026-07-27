class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            key=[0]*26
            for let in s:
                key[ord(let)-ord('a')]+=1
            key=tuple(key)

            if key in seen:
                seen[key].append(s)
            else:
                seen[key]=[s]
        
        res=[]
        for key, val in seen.items():
            res.append(val)

        return res