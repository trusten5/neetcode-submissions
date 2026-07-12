class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}

        for val in nums:
            if val in map1:
                map1[val]+=1
            else:
                map1[val] = 1

        top_k = [0] * k
        highest = [0] * k
        for key, value in map1.items():
            if value > min(highest):
                ind = highest.index(min(highest))
                highest[ind] = value
                top_k[ind] = key

        return top_k


        
