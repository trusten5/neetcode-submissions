class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = 0
        output = []
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            i = x + 1
            j = len(nums)-1
            while i < j:
                if nums[i] + nums[j] == -nums[x]:
                    output.append([nums[i], nums[j], nums[x]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] > -nums[x]:
                    j = j-1
                elif nums[i] + nums[j] < -nums[x]: 
                    i += 1

        return output