class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        small=1

        while True:
            if small not in nums:
                return small
            small+=1