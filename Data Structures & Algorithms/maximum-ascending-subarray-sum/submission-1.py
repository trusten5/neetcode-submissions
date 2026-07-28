class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_c = 0
        sums=0

        for i in range(len(nums)):
            sums+=nums[i]
            if i == len(nums)-1:
                max_c=max(max_c, sums)
            else:
                if nums[i]>=nums[i+1]:
                    max_c = max(max_c, sums)
                    sums=0

        
        return max_c