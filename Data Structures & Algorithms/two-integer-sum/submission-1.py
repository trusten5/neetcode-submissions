class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
        
        return output

        