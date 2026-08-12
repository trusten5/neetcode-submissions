class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        right = [i for i in range(1,len(nums)+1)]
        seen=[]
        missing=0
        swap=0
        for n in nums:
            if n in seen:
                swap=n
            seen.append(n)
        for n in right:
            if n not in nums:
                missing = n
        
        return [swap, missing]

            
