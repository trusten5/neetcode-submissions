class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1={}
        for n in strs:
            key=[0]*26
            for letter in list(n):
                key[ord(letter)-ord('a')]+=1
            key=tuple(key)
            if key in map1:
                map1[key].append(n)
            else:
                map1[key] = [n]

        # result = []
        # for k, v in map1.items():
        #     result.append(v)
        
        return list(map1.values())
