class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[]for i in range(len(nums)+1)]
        seen={}
        out=[]
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1
        
        for keys, val in seen.items():
            freq[val].append(keys)

        for n in freq[::-1]:
            for num in n:
                out.append(num)
            if len(out)==k:
                return out
