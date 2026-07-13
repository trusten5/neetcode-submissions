class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        map2 = {}
        result = []
        for n in nums:
            if n in map2:
                map2[n] +=1
            else:
                map2[n] = 1
            
        for p, v in map2.items():
            freq[v].append(p)
        
        print(freq)

        for x in freq[::-1]:
            for num in x:
                result.append(num)
                print(result)
                print(len(result))
                print(k)
                print(len(result)==k)
                if len(result) == k:
                    return result
        

             