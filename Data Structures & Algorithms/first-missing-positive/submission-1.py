class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        seen = [False]*len(nums)

        for n in nums:
            if n <= len(nums) and n>0:
                seen[n-1]=True
        
        for n in range(len(seen)):
            if seen[n] == False:
                return n+1
        
        return len(nums)+1