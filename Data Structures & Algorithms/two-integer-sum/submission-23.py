class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}

        for n in range(len(nums)):
            if nums[n] in map1:
                return [map1[nums[n]],n]
            map1[target-nums[n]]=n