class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mindif = float('inf')
        i=0
        j=k-1
        nums.sort()
        while j<len(nums):
            mindif=min(mindif, nums[j]-nums[i])
            i+=1
            j+=1
        
        return mindif