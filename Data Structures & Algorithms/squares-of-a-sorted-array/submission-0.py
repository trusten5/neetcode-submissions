class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        res=[]

        while i<=j:
            if nums[j]<abs(nums[i]):
                res.append(nums[i]**2)
                i+=1
            else:
                res.append(nums[j]**2)
                j-=1
        
        return res[::-1]
            


        
