class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        out=[]
        seen={}

        for n in strs:
            key = [0]*26
            for l in n:
                key[ord(l)-ord('a')]+=1
            key = tuple(key)
            if key in seen:
                seen[key].append(n)
            else:
                seen[key]=[n]
        
        for k, v in seen.items():
            out.append(v)

        return out