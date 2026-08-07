class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        count={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        
        for keys, vals in count.items():
            freq[vals].append(keys)
        res=[]
        for lis in freq[::-1]:
            for n in lis:
                res.append(n)
            if len(res)==k:
                return res