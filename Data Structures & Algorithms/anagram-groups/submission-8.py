class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1={}

        for word in strs:
            key = [0]*26
            for s in word:
                key[ord(s)-ord('a')]+=1
            if tuple(key) in map1:
                map1[tuple(key)].append(word)
            else:
                map1[tuple(key)]=[word]
        print(map1.items())
        result = []
        for k, v in map1.items():
            result.append(v)

        return result