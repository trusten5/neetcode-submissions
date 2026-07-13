class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i=0
        while i<len(nums):
            product = 1
            j=0
            while j<len(nums):
                if j == i:
                    j+=1
                else:
                    product = product*nums[j]
                    j+=1
            result[i] = product
            i+=1

        return result

