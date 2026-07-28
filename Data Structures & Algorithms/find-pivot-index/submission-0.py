class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = [0]*(len(nums)+1)

        for i in range(len(nums)):
            res[i+1]=res[i]+nums[i]

        for i in range(len(nums)):
            if res[i]==(res[-1]-res[i+1]):
                return i
        
        return -1


            
