class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

    
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in maps:
                return [maps[diff], i]
            maps[nums[i]] = i
