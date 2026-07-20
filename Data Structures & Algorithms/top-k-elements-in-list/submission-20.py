class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums))]
        map1={}

        for n in nums:
            if n in map1:
                map1[n]+=1
            else:
                map1[n]=1
        for key, value in map1.items():
            freq[value-1].append(key)

        result = []
        for n in freq[::-1]:
            for num in n:
                result.append(num)
            if len(result)==k:
                return result
