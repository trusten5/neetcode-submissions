class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = [0]*len(nums)

        for i in range(len(nums)):
            map1[i] = target-nums[i]

        for i in range(len(nums)):
            if nums[i] in map1[i+1:] and map1.index(nums[i], i+1) != i:
                return [i, map1.index(nums[i], i+1)]

