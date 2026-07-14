class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1={}
        for x in nums:
            if x in map1:
                return True
            else:
                map1[x] = 1
        
        return False