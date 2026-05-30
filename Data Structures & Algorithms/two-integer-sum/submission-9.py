class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                j+=1
            
            i+=1
            j = 1
                