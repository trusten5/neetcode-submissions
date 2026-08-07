class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*(len(nums))
        prefix=1

        for n in range(len(nums)):
            res[n]=prefix
            prefix*=nums[n]
        
        suffix=1
        for n in range(len(nums)-1, -1, -1):
            res[n]*=suffix
            suffix*=nums[n]
        
        return res