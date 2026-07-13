class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for x in range(len(nums)):
            if nums[x] in map1 and x != map1[nums[x]]:
                return [map1[nums[x]],x]
            diff = target-nums[x]
            map1[diff] = x
            