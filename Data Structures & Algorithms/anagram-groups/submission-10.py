class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}

        for word in strs:
            key=[0]*26
            for l in word:
                key[ord(l)-ord('a')]+=1
            key=tuple(key)
            if key in seen:
                seen[key].append(word)
            else:
                seen[key]=[word]

        res=[]
        for keys, values in seen.items():
            res.append(values)

        return res
