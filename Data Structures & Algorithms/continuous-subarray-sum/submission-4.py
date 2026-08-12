class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        i=0
        while i< len(nums):
            j=i
            count = 0
            
            while j<len(nums):
                count+=nums[j]
                if (j-i>0) and count%k ==0:
                    return True
                j+=1
                
            i+=1
        return False