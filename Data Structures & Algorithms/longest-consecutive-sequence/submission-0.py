class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        counter = 0
        output = 0

        for x in num_set:
            if x-1 not in num_set:
                while (x+counter) in num_set:
                    counter += 1
                if counter > output:
                    output = counter
                counter = 0

        return output