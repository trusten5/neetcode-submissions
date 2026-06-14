class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        running = 1
        for x in nums:
            out.append(running)
            running = running*x
        
        running = 1

        for y in range(len(nums)-1, -1, -1):
            out[y] = out[y] * running
            running = running* nums[y]

        return out

        
            

