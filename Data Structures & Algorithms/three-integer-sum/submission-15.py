class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for x, a in enumerate(nums):
            if a > 0:
                break
            
            if x>0 and a == nums[x-1]:
                continue
            
            i = x+1
            j = len(nums)-1

            while i<j:
                tsum = a+nums[i]+nums[j]
                if tsum>0:
                    j-=1
                elif tsum<0:
                    i+=1
                elif tsum == 0:
                    res.append([a, nums[i], nums[j]])
                    
                    i+=1
                    j-=1
                    
                    while nums[i]==nums[i-1] and i<j:
                        i+=1

        return res                


