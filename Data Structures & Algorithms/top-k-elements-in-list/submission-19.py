class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            if n in map1:
                map1[n]+=1
            else:
                map1[n]=1
        
        result = []
        for key, v in map1.items():
            freq[v].append(key)

        for lists in freq[::-1]:
            for n in lists:
                result.append(n)
            if len(result)==k:
                return result
