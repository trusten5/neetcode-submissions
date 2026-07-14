class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_count=0
        
        for n in nums:
            i=1
            if n-1 in nums:
                continue
            else:
                count=1
                while n+i in nums:
                    print(n+i)
                    count+=1
                    i+=1
                if count>max_count:
                    max_count=count
                    count=0
        
        return max_count