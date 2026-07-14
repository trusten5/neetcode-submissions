class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        clean=nums
        for i in range(len(clean)):
            diff = -clean[i]
            map1={}
            for j in range(len(clean)):
                if i != j:
                    needed= diff-clean[j]
                    if needed in map1 and j != map1[needed]:
                        triplet = tuple(sorted([clean[i], clean[j], clean[map1[needed]]]))
                        result.add(triplet)
                    map1[clean[j]]=j
        return  [list(t) for t in result]
                

