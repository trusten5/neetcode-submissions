class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for x in range(len(nums)):
            diff = target-nums[x]
            map1[diff] = x
        for y in range(len(nums)):
            if nums[y] in map1 and y != map1[nums[y]]:
                return [y, map1[nums[y]]]