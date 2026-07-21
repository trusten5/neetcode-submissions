class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1={}
        for n in nums:
            if n in map1:
                return True
            else:
                map1[n]=1
        
        return False