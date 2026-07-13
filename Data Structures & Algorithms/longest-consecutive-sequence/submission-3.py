class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map1 = set(nums)
        longest = 0
        max_count = 0
        for num in map1:
            if num-1 not in map1:
                length = 1
                while num+length in map1:
                    length += 1
                if length > max_count:
                    max_count = length
        
        return max_count