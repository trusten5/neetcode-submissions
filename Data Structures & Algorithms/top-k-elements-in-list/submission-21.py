class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}

        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1
        
        freq=[[]for i in range(len(nums))]
        print(freq)
        for key, val in seen.items():
            freq[val-1].append(key)
        

        res = []
        for i in freq[::-1]:
            for num in i:
                res.append(num)
            if len(res)==k:
                return res


