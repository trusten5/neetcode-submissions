class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        for x in range(len(strs)):
            key = [0]*26
            # print(strs[x])
            for l in list(strs[x]):
                key[ord('a')-ord(l)] +=1
            key_t = tuple(key)
            if key_t in map1:
                map1[key_t].append(strs[x])
            else:
                map1[key_t] = [strs[x]]
        
        res = []
        for k, v in map1.items():
            res.append(v)
        
        print(map1.items())
        print(res)
        
        return res