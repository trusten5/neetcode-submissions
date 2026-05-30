class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1
            if hashmap[x] > 1:
                return True
        return False
                