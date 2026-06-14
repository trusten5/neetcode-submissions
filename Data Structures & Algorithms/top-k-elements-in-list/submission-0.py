class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}

        for x in nums:
            if x not in vals:
                vals[x] = 1
            else:
                vals[x] += 1

        final = [[] for j in range(len(nums)+1)]

        for x in vals:
            final[vals[x]].append(x)

        answer = []

        for x in final[::-1]:
            if x == []:
                pass
            else:
                for l in x:
                    answer.append(l)

        return answer[:k]

        