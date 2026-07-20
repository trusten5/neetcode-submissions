class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_c=0
        for n in nums:
            if not n-1 in nums:
                count=1
                while n+1 in nums:
                    count+=1
                    n+=1
                max_c=max(count, max_c)
        
        return max_c