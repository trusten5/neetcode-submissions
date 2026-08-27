class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        count = 0
        for n in nums:
            if n-1 not in nums:
                up = 1
                while n+1 in nums:
                    up+=1
                    n+=1
                count = max(count, up)
        
        return count