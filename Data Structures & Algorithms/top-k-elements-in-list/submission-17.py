class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        freq=[[] for i in range(len(nums) + 1)]
        print(freq)
        for x in nums:
            if x in map1:
                map1[x]+=1
            else:
                map1[x]=1
        
        print(map1)
        print(map1.items())
        
        for key, value in map1.items():
            print(key)
            print(value)
            freq[value-1].append(key)
            print(freq)
        
        print(freq)

        result = []
        for i in range(len(freq)-1, -1, -1):
            for val in freq[i]:
                result.append(val)
            if len(result)==k:
                return result