class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}

        for val in nums:
            if val in map1:
                map1[val]+=1
            else:
                map1[val] = 1

        freq = [[] for i in range(len(nums) + 1)]
        
        for key, value in map1.items():
            freq[value].append(key)
              

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



        
