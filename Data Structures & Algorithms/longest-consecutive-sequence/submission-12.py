class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_c = 0
        for n in nums:
            if n-1 not in nums:
                counter=0
                while n in nums:
                    counter+=1
                    n+=1
                max_c = max(max_c, counter)
        
        return max_c
