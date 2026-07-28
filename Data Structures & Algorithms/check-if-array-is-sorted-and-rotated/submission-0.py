class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        N = len(nums)
        
        for n in range(N):
            if nums[n]>nums[(n+1) % N]:
                count+=1
                if count>1:
                    return False
        
        return True