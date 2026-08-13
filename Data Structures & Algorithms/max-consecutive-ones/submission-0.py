class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mc=0
        count=0
        for n in nums:
            if n==1:
                count+=1
            else:
                mc=max(count, mc)
                count=0
        
        mc=max(count, mc)

        return mc