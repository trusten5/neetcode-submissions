class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy=nums.copy()
        length=len(nums)
        for n in range(len(dummy)):
            newind = (n+k)%length
            nums[newind]=dummy[n]

            # Pos+Shift%Len