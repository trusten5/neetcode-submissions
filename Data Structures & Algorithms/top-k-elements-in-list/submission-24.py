class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        seen={}

        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1

        for keys, vals in seen.items():
            freq[vals].append(keys)
        res=[]
        for lis in freq[::-1]:
            for i in lis:
                res.append(i)
            if len(res)==k:
                return res
