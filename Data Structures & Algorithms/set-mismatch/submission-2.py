class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        right = [i for i in range(1,len(nums)+1)]
        seen=[]
        missing=0
        swap=0

        for n in range(len(right)):
            if right[n] not in nums:
                missing = right[n]
            if nums[n] in seen:
                swap = nums[n]
            seen.append(nums[n])
            
            
        
        return [swap, missing]

            
