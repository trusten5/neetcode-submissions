class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        final_list=[]
        for x in strs:
            lists = list(x)
            sig = [0]*26
            for y in lists:
                sig[ord(y)-ord('a')]+=1
            if tuple(sig) in map1:
                map1[tuple(sig)].append(x)
            else:
                map1[tuple(sig)] = [x]

        for k, v in map1.items():
            final_list.append(v)

        return final_list
            


